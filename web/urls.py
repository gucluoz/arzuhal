from django.conf.urls import url

from . import views

urlpatterns = [
  url(r'^$', views.index, name='index'),
  url(r'^q/(?P<q>[a-zA-Z0-9\%\ ]+)$', views.indexsearch, name='indexsearch'),
  url(r'^a/', views.autoComplete, name='autocomplete'),
  url(r'^list/$', views.PetitionListView.as_view(), name='list'),
  url(r'^crawl/$', views.crawl, name='crawl'),
  url(r'^detail/(?P<name>[a-z_]+)$', views.detailByName, name='detailbyName'),
  url(r'^d/(?P<ticket>[A-Za-z0-9]{32})', views.download, name='download'),
]