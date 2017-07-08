from django.conf.urls import url
from django.contrib.sitemaps.views import sitemap
from . import views
from aroma.views import AromaCompactSearch
from main.views import ContactView
from main.sitemap import DinamicSitemap, StaticSitemap


sitemaps = {'articles': DinamicSitemap, 'static': StaticSitemap}

urlpatterns = [
    url(r'^$', AromaCompactSearch.as_view(), name='home'),
    url(r'^contacts/$', ContactView.as_view(), name='contacts'),
    url(r'^tos/$', views.tos, name='tos'),
    url(r'^sitemap.xml$', sitemap, {'sitemaps': sitemaps}),
]
