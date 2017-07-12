from django.conf.urls import url
from tag.views import TagsAutocomplete

urlpatterns = [
    url(r'^tags_autocomplete/$', TagsAutocomplete.as_view(), name='tags-autocomplete'),
]
