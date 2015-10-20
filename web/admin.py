from django.contrib import admin
from django.utils import timezone
from django import forms
import pdb;

from .models import Petition, Subject, Template, Keyword

class PetitionForm(forms.ModelForm):
  description = forms.CharField(max_length=200, widget=forms.Textarea)

  class Meta:
    model = Petition
    fields = ['name', 'subject', 'description', 'keywords', 'isActive', 'accessCount', 'downloadCount']

class TemplateInline(admin.StackedInline):
  extra = 1
  model = Template
  exclude = ['downloadticket', 'extension']

class PetitionAdmin(admin.ModelAdmin):
  form = PetitionForm
  inlines = [ TemplateInline, ]

  def save_model(save, request, obj, form, change):
    obj.publishedby = request.user
    obj.publishdate = timezone.now()
    obj.save()

admin.site.register(Petition, PetitionAdmin)
admin.site.register(Subject)
admin.site.register(Template)
admin.site.register(Keyword)