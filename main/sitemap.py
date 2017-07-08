from django.contrib.sitemaps import Sitemap
from aroma.models import Aroma
from django.core.urlresolvers import reverse


class DinamicSitemap(Sitemap):
    changefreq = "daily"
    priority = 0.5

    def items(self):
        return Aroma.objects.filter(is_public=True)

    def location(self, aroma):
        return aroma.get_absolute_url()


class StaticSitemap(Sitemap):
    changefreq = "weekly"
    priority = 0.5

    def items(self):
        return ['home', 'contacts', 'aroma-list', 'tos', 'notes-search']

    def location(self, object):
        return reverse(object)