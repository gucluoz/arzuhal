from django.contrib.sitemaps import Sitemap
from web.models import Petition

class ArzuhalSitemap(Sitemap):
  changefreq = "daily"
  priority = 0.5

  def items(self):
    return Petition.objects.filter(isActive=True)

  def lastmod(self, obj):
    return obj.publishdate