from django.shortcuts import get_object_or_404, redirect

from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

from activity.models import Activity, Comment
from aroma.models import Aroma


class ActivityCreate(generics.CreateAPIView):
    permission_classes = (IsAuthenticated,)
    activity_type = ''

    def post(self, request, *args, **kwargs):
        aroma = get_object_or_404(Aroma, id=kwargs.get('aroma_id'))
        aroma.marks.get_or_create(activity_type=self.activity_type, user=request.user)
        return redirect(request.META.get('HTTP_REFERER'))


class ActivityDelete(generics.DestroyAPIView):
    permission_classes = (IsAuthenticated,)
    activity_type = ''

    def get(self, request, *args, **kwargs):
        Activity.objects.get(pk=kwargs.get('pk')).delete()
        return redirect(request.META.get('HTTP_REFERER'))


class VoteAdd(generics.CreateAPIView):
    permission_classes = (IsAuthenticated,)
    activity_type = ''

    def post(self, request, *args, **kwargs):
        comment = get_object_or_404(Comment, id=kwargs.get('comment_id'))
        vote, created = comment.votes.get_or_create(user=request.user)
        if created:
            comment.rating += 1
            comment.save()
        return redirect(request.META.get('HTTP_REFERER')+'#comments')
