from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from .views import AromaList, AromaDetail

urlpatterns = [
    url(r'^aromas/$', AromaList.as_view(), name='aroma-list'),
    url(r'^aromas/(?P<pk>[0-9]+)/$', AromaDetail.as_view(), name='aroma-detail'),
]

# Format suffixes
urlpatterns = format_suffix_patterns(urlpatterns, allowed=['json', 'api'])
