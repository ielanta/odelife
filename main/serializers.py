from aroma.models import Aroma
from rest_framework import serializers
from activity.serializers import AromaCommentSerializer
from activity.models import Comment


class UpdatedAromasListSerializer(serializers.ModelSerializer):
    tags = serializers.SerializerMethodField()

    @staticmethod
    def get_tags(obj):
        return obj.get_tags()

    class Meta:
        model = Aroma
        fields = ('guise', 'url', 'title', 'tags', 'description')
        extra_kwargs = {
            'url': {'lookup_field': 'slug'}
        }


class NewCommentsListSerializer(AromaCommentSerializer):
    aroma_title = serializers.CharField(read_only=True, source='aroma.title')

    class Meta:
        model = Comment
        fields = ('id',  'text',  'aroma_pic', 'user', 'aroma_url', 'aroma_title')
