from django.contrib import admin

from .models import Petition, Subject, Template, Meta, Keyword

admin.site.register(Petition)
admin.site.register(Subject)
admin.site.register(Template)
admin.site.register(Meta)
admin.site.register(Keyword)