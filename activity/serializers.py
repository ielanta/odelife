from rest_framework import serializers

from accounts.serializers import UserSerializer
from activity.models import Comment


class CommentSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    longevity = serializers.SerializerMethodField()
    sillage = serializers.SerializerMethodField()
    season = serializers.SerializerMethodField()
    impression = serializers.SerializerMethodField()
    tags = serializers.SerializerMethodField()

    @staticmethod
    def get_longevity(obj):
        return obj.get_longevity_display()

    @staticmethod
    def get_sillage(obj):
        return obj.get_sillage_display()

    @staticmethod
    def get_season(obj):
        icon_dict = {'SP': ['spring.png'], 'SM': ['summer.png'], 'A': ['autumn.png'], 'W': ['winter.png'],
                     'E': ['spring.png', 'summer.png', 'autumn.png', 'winter.png']}
        if icon_dict.get(obj.season):
            return {obj.get_season_display(): icon_dict.get(obj.season)}

    @staticmethod
    def get_impression(obj):
        icon_dict = {'F': 'love.png', 'L': 'like.png', 'N': 'neutral.png', 'D': 'dislike.png'}
        return {obj.get_impression_display(): icon_dict.get(obj.impression)}

    @staticmethod
    def get_tags(obj):
        return [ti.tag for ti in obj.taggeditems.all()]

    class Meta:
        model = Comment
        fields = ('id', 'user', 'impression', 'longevity', 'sillage', 'season', 'text', 'rating', 'tags')



class AromaCommentSerializer(CommentSerializer):
    aroma_pic = serializers.ImageField(read_only=True, source='aroma.pic')
    aroma_url = serializers.SerializerMethodField()

    @staticmethod
    def get_aroma_url(obj):
        return obj.aroma.get_absolute_url()

    class Meta:
        model = Comment
        fields = ('id', 'impression', 'longevity', 'sillage', 'season', 'text', 'rating', 'aroma_pic',
                  'aroma_url')
