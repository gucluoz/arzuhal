# -*- coding: UTF-8 -*-

from django.conf.urls import url

from . import views

urlpatterns = [
  url(r'^$', views.index, name='index'),
  url(u'^q/(?P<q>[a-zA-ZğüşıöçĞÜŞİÖÇ0-9\%\ ]+)$', views.indexsearch, name='indexsearch'),
  url(r'^a/', views.autoComplete, name='autocomplete'),
  url(r'^list/$', views.PetitionListView.as_view(), name='list'),
  url(r'^detail/(?P<name>[a-z0-9_]+)$', views.detailByName, name='detailbyName'),
  url(r'^d/(?P<ticket>[A-Za-z0-9]{32})', views.download, name='download'),
  url(r'^kanun/', views.kanunHtml, name='kanunHtml'),
  url(r'^nasil/yazilir/', views.nasilYazilirHtml, name='nasilYazilirHtml'),
]