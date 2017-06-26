from django.conf.urls import url
from aroma.views import BrandAutocomplete, AromaDetail, AromaList, GroupsAutocomplete, NosesAutocomplete, \
    NotesAutocomplete, NoteCompactSearch

urlpatterns = [
    url(r'^$', AromaList.as_view(), name='aroma-list'),
    url(r'^notes/$', NoteCompactSearch.as_view(), name='notes-search'),
    url(r'^brand_autocomplete/$', BrandAutocomplete.as_view(), name='brand-autocomplete'),
    url(r'^group_autocomplete/$', GroupsAutocomplete.as_view(), name='groups-autocomplete'),
    url(r'^nose_autocomplete/$', NosesAutocomplete.as_view(), name='noses-autocomplete'),
    url(r'^note_autocomplete/$', NotesAutocomplete.as_view(), name='notes-autocomplete'),
    url(r'^(?P<slug>[\w\d\-\_]+)/$', AromaDetail.as_view(), name='aroma-detail'),
]