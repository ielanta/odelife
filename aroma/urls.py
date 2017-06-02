from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^brand_autocomplete/$', views.BrandAutocomplete.as_view(), name='brand-autocomplete'),
    url(r'^note_autocomplete/$', views.NotesAutocomplete.as_view(), name='notes-autocomplete'),
    url(r'^group_autocomplete/$', views.GroupAutocomplete.as_view(), name='group-autocomplete'),
    url(r'^nose_autocomplete/$', views.NosesAutocomplete.as_view(), name='noses-autocomplete'),
]