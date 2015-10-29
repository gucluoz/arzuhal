from django.conf.urls import include, url
from django.contrib import admin
from django.contrib.sitemaps.views import sitemap
from sitemaps import ArzuhalSitemap

sitemaps = {
  'arzuhal' : ArzuhalSitemap()
}

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^web/', include('web.urls')),
    url(r'^harita\.xml$', sitemap, {'sitemaps': sitemaps},
      name='django.contrib.sitemaps.views.sitemap'),
]
