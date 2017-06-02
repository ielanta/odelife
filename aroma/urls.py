from django.conf.urls import url
from aroma import views

urlpatterns = [
    url(r'^$', views.AromaList.as_view(), name='aroma-list'),
    url(r'^(?P<pk>[0-9]+)/$', views.AromaDetail.as_view(), name='aroma-detail'),
    url(r'^brand_autocomplete/$', views.BrandAutocomplete.as_view(), name='brand-autocomplete'),
    url(r'^group_autocomplete/$', views.GroupAutocomplete.as_view(), name='group-autocomplete'),
    url(r'^nose_autocomplete/$', views.NosesAutocomplete.as_view(), name='noses-autocomplete'),
    url(r'^note_autocomplete/$', views.NotesAutocomplete.as_view(), name='notes-autocomplete'),
]