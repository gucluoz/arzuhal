from django.conf.urls import include, url
from django.contrib import admin
from django.contrib.sitemaps.views import sitemap
from sitemaps import ArzuhalSitemap
from django.views.generic import TemplateView

sitemaps = {
  'arzuhal' : ArzuhalSitemap()
}

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^web/', include('web.urls')),
    url(r'^harita\.xml$', sitemap, {'sitemaps': sitemaps},
      name='django.contrib.sitemaps.views.sitemap'),
    url(r'^robots\.txt$', TemplateView.as_view(
      template_name='robots.txt', content_type='text/plain')),
]
