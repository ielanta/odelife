from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from .views import AromaList

urlpatterns = [
    url(r'^aromas/$', AromaList.as_view(), name='aroma-list'),
]

# Format suffixes
urlpatterns = format_suffix_patterns(urlpatterns, allowed=['json', 'api'])
