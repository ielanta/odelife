from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^(?P<id>[0-9]+)/$', views.get_aroma, name='get_aroma'),
    url(r'^brand-autocomplete/$', views.BrandAutocomplete.as_view(), name='brand-autocomplete'),
]