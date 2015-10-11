# -*- coding: UTF-8 -*-

import binascii
import os
from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

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
  name = models.CharField(max_length=200)
  publishdate = models.DateTimeField('Date first published', default=timezone.now)
  publishedby = models.ForeignKey(User)
  subject = models.ForeignKey(Subject)
  keywords = models.ManyToManyField(Keyword)
  description = models.CharField(max_length=1000)
  ascii_filename = models.CharField(max_length=200, blank=True)

  def save(self):
    super(Petition, self).save()
    self.ascii_filename = filenameify(self.name)[:80]
    super(Petition, self).save()

  def __unicode__(self):
    return self.name

class Template(models.Model):
  version = models.IntegerField(default=1)
  filename = models.FileField(upload_to=generate_download_ticket)
  extension = models.CharField(max_length=10, blank=True, null=True)
  petition = models.ForeignKey(Petition)
  downloadticket = models.CharField(max_length=32, blank=True, null=True)
  publishdate = models.DateTimeField('Date first published', default=timezone.now)
  publishedby = models.ForeignKey(User)

  def __unicode__(self):
    return self.petition.name + " " + str(self.version)