from django.db import models
from django.contrib.auth.models import User

class Subject(models.Model):
  name = models.CharField(max_length=200)
  containerdirectory = models.CharField(max_length=50)

class Petition(models.Model):
  name = models.CharField(max_length=200)
  publishdate = models.DateTimeField('Date first published')
  publishedby = models.ForeignKey(User)
  subject = models.ForeignKey(Subject)

  def __str__(self):
    return self.name

class Template(models.Model):
  version = models.IntegerField(default=1)
  filename = models.CharField(max_length=100)
  petition = models.ForeignKey(Petition)

  def __str__(self):
    return self.petition.name % " " % self.version

class Meta(models.Model):
  petition = models.ForeignKey(Petition)
  maxlength = models.IntegerField(default=100)

  def __str__(self):
    return self.name

class Keyword(models.Model):
  name = models.CharField(max_length=30)

  def __str__(self):
    return self.name