from django.shortcuts import render, get_object_or_404
from django.views import generic

from .models import Petition

class PetitionListView(generic.ListView):
  template_name = 'web/petitionlist.html.j2'
  model = Petition

  def get_queryset(self):
    return Petition.objects.order_by('-publishdate')

class PetitionDetailView(generic.DetailView):
  template_name = 'web/petitiondetail.html.j2'
  model = Petition

def index(request):
  return render(request, 'web/index.html.j2')

"""
Su anda kullanilamiyor

def petitionDetail(request, pk):
  petition = get_object_or_404(Petition, pk=pk)
  context = {'petition' : petition}
  return render(request, 'web/petitiondetail.html.j2', context)

"""