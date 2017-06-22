from django.conf.urls import url
from . import views
from aroma.views import AromaCompactSearch
from main.views import ContactView

urlpatterns = [
    url(r'^$', AromaCompactSearch.as_view(), name='home'),
    url(r'^contacts/$', ContactView.as_view(), name='contacts'),
    url(r'^tos/$', views.tos, name='tos'),
]
