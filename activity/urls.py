from django.conf.urls import url
from activity.views import ActivityCreate, ActivityDelete, VoteAdd, CommentCreate
from activity.models import Activity

urlpatterns = [
    url(r'^aromas/(?P<aroma_id>[0-9]+)/favorites/$', ActivityCreate.as_view(activity_type=Activity.FAVORITE),
        name='add-favorite'),
    url(r'^aromas/(?P<aroma_id>[0-9]+)/favorites/(?P<pk>[0-9]+)/$', ActivityDelete.as_view(activity_type=Activity.FAVORITE),
        name='delete-favorite'),
    url(r'^aromas/(?P<aroma_id>[0-9]+)/likes/$', ActivityCreate.as_view(activity_type=Activity.LIKE), name='add-like'),
    url(r'^aromas/(?P<aroma_id>[0-9]+)/likes/(?P<pk>[0-9]+)/$', ActivityDelete.as_view(activity_type=Activity.LIKE),
        name='delete-like'),
    url(r'^comments/(?P<comment_id>[0-9]+)/votes/$', VoteAdd.as_view(), name='add-vote'),
    url(r'^aromas/(?P<aroma_id>[0-9]+)/comments/$', CommentCreate.as_view(), name='add-comment'),
]
