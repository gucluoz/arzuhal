# -*- coding: UTF-8 -*-

import binascii
import os
from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.core.urlresolvers import reverse

def generate_download_ticket(instance, filename):
  extension = filename.split('.')[-1]
  ticket = binascii.hexlify(os.urandom(16))
  instance.downloadticket = ticket
  if extension == filename:
    extension = ''
  instance.extension = extension
  return ticket

def filenameify(data):
  dict = {
    u'ğ' : u'g',
    u'ü' : u'u',
    u'ş' : u's',
    u'ç' : u'c',
    u'ö' : u'o',
    u'ı' : u'i',
    u'Ğ' : u'g',
    u'Ü' : u'u',
    u'Ş' : u's',
    u'Ç' : u'c',
    u'Ö' : u'o',
    u'İ' : u'i',
    u'?' : u'',
    u' ' : u'_',
    u'.' : u'',
    u',' : u'',
    u'/' : u'',
    u'\\' : u'',
    u'+' : u'',
    u'&' : u'',
    u'^' : u'',
    u'!' : u'',
    u'*' : u'',
    u'-' : u'',
    u'(' : u'',
    u')' : u'',
    u'=' : u'',
  }

  for letter in dict:
    data = data.replace(letter, dict[letter])
  data = data.lower()

  return data

class Subject(models.Model):
  name = models.CharField(max_length=200)

  def __unicode__(self):
    return self.name

class Keyword(models.Model):
  name = models.CharField(max_length=30)

  def __unicode__(self):
    return self.name

class Petition(models.Model):
  name = models.CharField('İsim', max_length=200)
  publishdate = models.DateTimeField('Date first published', default=timezone.now)
  publishedby = models.ForeignKey(User)
  subject = models.ForeignKey(Subject,verbose_name='Konu')
  keywords = models.ManyToManyField(Keyword, blank=True, verbose_name='Anahtar Kelimeler')
  description = models.TextField(verbose_name='Açıklama')
  ascii_filename = models.CharField(max_length=200, blank=True, verbose_name='URL Görünen Ad [Dikkat!]')
  accessCount = models.IntegerField(default=0,verbose_name='Görüntüleme')
  downloadCount = models.IntegerField(default=0,verbose_name='İndirme')
  isActive = models.BooleanField(default=True,verbose_name='Aktif?')
  retainAsciiFilename = True

  def save(self):
    super(Petition, self).save()
    if self.ascii_filename and self.retainAsciiFilename:
      return
    self.ascii_filename = filenameify(self.name)[:80]
    super(Petition, self).save()

  def get_absolute_url(self):
    return reverse('detailbyName',args=[self.ascii_filename])

  def __unicode__(self):
    return self.name

class Template(models.Model):
  version = models.IntegerField(default=1)
  filename = models.FileField(upload_to=generate_download_ticket,verbose_name='Dosya adı')
  extension = models.CharField(max_length=10, blank=True, null=True,verbose_name='Uzantı')
  petition = models.ForeignKey(Petition)
  downloadticket = models.CharField(max_length=32, blank=True, null=True)
  publishdate = models.DateTimeField(default=timezone.now,verbose_name='Yayın Tarihi')
  publishedby = models.ForeignKey(User, verbose_name='Yayınlayan')

  def __unicode__(self):
    return self.petition.name + " " + str(self.version)

class SearchRecord(models.Model):
  keyword = models.CharField(max_length=200, verbose_name='Arama metni')
  searchTime = models.DateTimeField(default=timezone.now, verbose_name='Arama tarihi')
  resultcount = models.IntegerField(default=0)

  def __unicode__(self):
    return self.keyword


