import binascii
import os
from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

def generate_download_ticket(instance, filename):
  extension = filename.split('.')[-1:]
  ticket = binascii.hexlify(os.urandom(16))
  instance.downloadticket = ticket
  if extension == filename:
    extension = ''
  instance.extension = extension
  return ticket

class Subject(models.Model):
  name = models.CharField(max_length=200)
  containerdirectory = models.CharField(max_length=50)

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
    self.ascii_filename = self.name.lower().encode('ascii','ignore').replace(' ','_').replace('?','').replace(',','').replace('(','').replace(')','').replace('.','')[:80]
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