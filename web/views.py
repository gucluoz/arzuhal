import time
import json
import datetime
import os
from django.shortcuts import render, get_object_or_404
from django.views import generic
from django.http import HttpResponse
from django.core.servers.basehttp import FileWrapper
from haystack.query import SearchQuerySet
from django.core.urlresolvers import reverse

from .models import Petition, Template, Subject


class PetitionListView(generic.ListView):
  template_name = 'web/petitionlist.html.j2'
  model = Petition

  def get_queryset(self):
    return Petition.objects.order_by('-publishdate')

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
    response = HttpResponse(FileWrapper(open(template.filename.path)),content_type='application/vnd.openxmlformats-officedocument.wordprocessingml.document')
    response['Content-Disposition'] = 'attachment; filename=' + template.petition.ascii_filename + '_v' + str(template.version) + '.' + template.extension
  except:
    return HttpResponse(status=404)
  return response


def detailByName(request, name):
  petition = get_object_or_404(
    Petition.objects.filter(ascii_filename=name))
  context = {'petition': petition, 'templates_ordered': petition.template_set.order_by('-version')}
  if context['templates_ordered'].count > 0:
      context['first_url'] = reverse('download', args=[context['templates_ordered'].first().downloadticket])

  return render(request, 'web/petitiondetail.html.j2', context)

from bs4 import BeautifulSoup as Bs
import re, urllib, binascii, os, urlparse, csv
from django.contrib.auth.models import User
from django.utils import timezone

def generateSoup(fileName):
  f = open(fileName)
  text = f.read()
  soup = Bs(text,from_encoding='iso-8859-9')
  f.close()
  return soup

def parseListtd(tdTag):
  return 'http://www.dilekceyaz.net/' + tdTag.a.get('href')

def parseAllList(soup):
  res = []
  for td in soup.find_all('td'):
    res.append(parseListtd(td))

  return res

def parseDetail(soup):
  #subject = re.findall(u'(?<=Di\xf0er  )(.*)(?= \xddle \xddlgili Dilek\xe7e \xd6rnekleri)',soup.find(id='MainContent_HyperLink1').text)[0]
  subject = soup.find(id='MainContent_HyperLink1').text.split(' ')[2]
  link = soup.find(id='MainContent_dilekce_htmgoster').get('src').replace('dilekceler_htm','http://www.dilekceyaz.net/dilekceler').replace('.htm','.doc')
  print('-parseDetail() -> '+subject)
  ret = {
    'text' : soup.find(id='MainContent_konu').text.replace('\n','').strip(),
    'subject' : subject.replace('\n','').strip(),
    'link' : link.replace('\n','').strip()
  }
  print('+parseDetail() -> '+ret['subject'])

  return ret;

def downloadContent(url):
  try:
    sock = urllib.urlopen(url.encode('iso-8859-9'))
    return sock.read()
  finally:
    sock.close()

def downloadFile(url, filename):
    urllib.urlretrieve(url.encode('iso-8859-9'),'petitions/' + filename)

def generateFileName():
  return binascii.hexlify(os.urandom(16))

def appendToFile(detail, name, extension):
  sub = Subject.objects.filter(name=detail['subject'])
  if not sub:
    sub = Subject(name=detail['subject'])
    sub.save()
    print('Subject save -> DONE')

  pet = Petition()
  pet.name = detail['text']
  pet.subject = Subject.objects.filter(name=detail['subject']).get()
  pet.publishdate = timezone.now()
  pet.publishedby = User.objects.all()[0]
  pet.description = detail['text']
  pet.save()
  print('Petition save -> DONE')
  template = Template()
  template.version = 1
  template.filename = name
  template.extension = extension
  template.petition = pet
  template.publishdate = timezone.now()
  template.publishedby = User.objects.all()[0]
  template.save()
  print('Template save -> DONE')

def crawl(request):
  petList = parseAllList(generateSoup('/Users/gucluozturk/Projects/dilekce_crawler/crawler/list.xml'))
  for pet in petList:
    try:
      print('FETCHING :' + pet + '...')
      detailText = downloadContent(pet)
      print('DONE')
      detailSoup = Bs(detailText, from_encoding='iso-8859-9')
      detail = parseDetail(detailSoup)

      filename = generateFileName()
      split = urlparse.urlsplit(detail['link'])
      fileextension = split.path.split('/')[-1].split('.')[-1]
      print('DOWNLOADING :' + detail['link'] + '...')
      downloadFile(detail['link'],filename)
      print('DONE')

      appendToFile(detail,filename, fileextension)

      print(detail['subject'])
      print(detail['text'])
      print(filename + '.' + fileextension)
      print('-------------------------------')
    except:
      print('************ ERROR ************')
  return HttpResponse(status=200)