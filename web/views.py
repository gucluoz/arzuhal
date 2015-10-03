import time
import json
from django.shortcuts import render, get_object_or_404
from django.views import generic
from django.http import HttpResponse
from haystack.query import SearchQuerySet

from .models import Petition


class PetitionListView(generic.ListView):
  template_name = 'web/petitionlist.html.j2'
  model = Petition

  def get_queryset(self):
    return Petition.objects.order_by('-publishdate')


class PetitionDetailView(generic.DetailView):
  template_name = 'web/petitiondetail.html.j2'
  model = Petition


def indexsearch(request, q):
  searchStartTime = time.time()
  results = SearchQuerySet().auto_query(q)[:100]
  searchElapsedTime = (time.time() - searchStartTime)*1000

  print 'Sarch request took -> %.3f ms' % searchElapsedTime 

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
    suggestions = [' '.join(result.text.split(' ')[:5]).strip() for result in sqs]
    suggestion_data = json.dumps({
      'results': suggestions
      })

    return HttpResponse(suggestion_data, content_type='application/json')
  except:

    return HttpResponse(status=404)