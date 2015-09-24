from django.conf.urls import url

from . import views

urlpatterns = [
  url(r'^$', views.index, name='index'),
  url(r'^list/$', views.PetitionListView.as_view(), name='list'),
  url(r'^detail/(?P<pk>[0-9]+)$', views.PetitionDetailView.as_view(), name='detail'),
]