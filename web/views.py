import time
import json
import datetime
import os
from django.shortcuts import render, get_object_or_404
from django.views import generic
from django.http import HttpResponse
from django.db.models import Count
from django.core.servers.basehttp import FileWrapper
from haystack.query import SearchQuerySet
from django.core.urlresolvers import reverse
from .models import Petition, Template, Subject

class PetitionListView(generic.ListView):
  template_name = 'web/petitionlist.html.j2'
  model = Petition

  def get_queryset(self):
    return Petition.objects.order_by('-publishdate')

def subjectList():
  subjects = Subject.objects.annotate(count=Count('petition')).order_by('-count')[:100]
  return subjects

def getLatestPetitions():
  return Petition.objects.filter(isActive=True).order_by('-publishdate')[:10]

def indexsearch(request, q):
  searchStartTime = time.time()
  results = SearchQuerySet().auto_query(q)[:100]
  searchElapsedTime = (time.time() - searchStartTime)*1000
  resultSet = []
  for r in results:
    resultSet.append(r.object)
  context = {
    'results' : resultSet,
    'q' : q,
    'searchTime' : searchElapsedTime,
    'subjects' : subjectList(),
  }
  #If search results are empty, show latest 5
  #if len(resultSet) == 0:
  
  #show either way
  context.update({'latestPetitions': getLatestPetitions()})

  return render(request, 'web/index.html.j2', context)

def index(request):
  try:
    searchString = request.POST['q']
    return indexsearch(request,searchString)
  except:
    return render(request, 'web/index.html.j2',{'subjects': subjectList(),'latestPetitions': getLatestPetitions()})

def autoComplete(request):
  try:
    searchString = request.GET['q']
    sqs = SearchQuerySet().autocomplete(content_auto=searchString)
    suggestions = [' '.join(result.object.name.split(' ')).strip() for result in sqs]
    suggestion_data = json.dumps({
      'results': suggestions
      })
    return HttpResponse(suggestion_data, content_type='application/json')
  except:
    return HttpResponse(status=404)

def download(request, ticket):
  template = get_object_or_404(
    Template.objects.filter(downloadticket=ticket))
  try:
    #Increment download count
    template.petition.downloadCount += 1
    template.petition.save()

    response = HttpResponse(FileWrapper(open(template.filename.path)),content_type='application/vnd.openxmlformats-officedocument.wordprocessingml.document')
    response['Content-Disposition'] = 'attachment; filename=' + template.petition.ascii_filename + '_v' + str(template.version) + '.' + template.extension
  except:
    return HttpResponse(status=404)
  return response


def detailByName(request, name):
  petition = get_object_or_404(
    Petition.objects.filter(ascii_filename=name))

  #Increment view count
  petition.accessCount += 1
  petition.save()

  if petition.template_set.count() == 0:
    return HttpResponse(status=404)
  context = {'petition': petition, 'templates_ordered': petition.template_set.order_by('-version')}
  if context['templates_ordered'].count > 0:
    context['first_url'] = reverse('download', args=[context['templates_ordered'].first().downloadticket])

  return render(request, 'web/petitiondetail.html.j2', context)

def kanunHtml(request):
  return render(request,'web/dilekcekanun.html.j2')