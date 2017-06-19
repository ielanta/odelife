from django.conf.urls import url
from activity.views import ActivityCreate, ActivityDelete
from activity.models import Activity

urlpatterns = [
    url(r'^favorites/(?P<aroma_id>[0-9]+)$', ActivityCreate.as_view(activity_type=Activity.FAVORITE),
        name='add-favorite'),
    url(r'^favorites/(?P<aroma_id>[0-9]+)/(?P<pk>[0-9]+)$', ActivityDelete.as_view(activity_type=Activity.FAVORITE),
        name='delete-favorite'),
    url(r'^likes/(?P<aroma_id>[0-9]+)$', ActivityCreate.as_view(activity_type=Activity.LIKE), name='add-like'),
    url(r'^likes/(?P<aroma_id>[0-9]+)/(?P<pk>[0-9]+)$', ActivityDelete.as_view(activity_type=Activity.LIKE),
        name='delete-like'),
]
