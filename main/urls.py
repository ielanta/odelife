from django.conf.urls import url
from . import views
from aroma.views import AromaCompactSearch

urlpatterns = [
    url(r'^$', AromaCompactSearch.as_view(), name='home'),
    url(r'^contacts/$', views.contacts, name='contacts'),
]