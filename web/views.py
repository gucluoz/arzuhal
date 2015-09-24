import time
from django.shortcuts import render, get_object_or_404
from django.views import generic
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
  searcStartTime = time.time()
  results = SearchQuerySet().auto_query(q)
  searchElapsedTime = (time.time() - searcStartTime)*1000
  #print "Search request -> %.3f ms" % searchElapsedTime
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

"""
Su anda kullanilamiyor

def petitionDetail(request, pk):
  petition = get_object_or_404(Petition, pk=pk)
  context = {'petition' : petition}
  return render(request, 'web/petitiondetail.html.j2', context)

"""