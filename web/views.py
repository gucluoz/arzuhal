import time
import json
import datetime
import os
from django.shortcuts import render, get_object_or_404
from django.views import generic
from django.http import HttpResponse
from django.core.servers.basehttp import FileWrapper
from haystack.query import SearchQuerySet

from .models import Petition, Template


class PetitionListView(generic.ListView):
  template_name = 'web/petitionlist.html.j2'
  model = Petition

  def get_queryset(self):
    return Petition.objects.order_by('-publishdate')


class PetitionDetailView(generic.DetailView):
  template_name = 'web/petitiondetail.html.j2'
  model = Petition

  def get_context_data(self, **kwargs):
    context = super(PetitionDetailView, self).get_context_data(**kwargs)
    context['templates_ordered'] = context['petition'].template_set.order_by('-version')
    return context


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
  }

  return render(request, 'web/index.html.j2', context)


def index(request):
  try:
    searchString = request.POST['q']
    return indexsearch(request,searchString)
  except:
    return render(request, 'web/index.html.j2')

def autoComplete(request):
  try:
    searchString = request.GET['q']
    sqs = SearchQuerySet().autocomplete(content_auto=searchString)[:5]
    suggestions = [' '.join(result.object.name.split(' ')[:5]).strip() for result in sqs]
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
    response = HttpResponse(FileWrapper(open(os.path.dirname(os.path.abspath(__file__)) + '/petitions/' + template.petition.subject.containerdirectory + '/' + template.filename)),content_type='application/vnd.openxmlformats-officedocument.wordprocessingml.document')
    response['Content-Disposition'] = 'attachment; filename=' + template.petition.ascii_filename
  except:
    return HttpResponse(status=404)
  return response


def detailByName(request, name):
  petition = get_object_or_404(
    Petition.objects.filter(ascii_filename=name))
  context = {'petition': petition, 'templates_ordered': petition.template_set.order_by('-version')}

  return render(request, 'web/petitiondetail.html.j2', context)