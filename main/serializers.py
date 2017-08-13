from aroma.models import Aroma
from rest_framework import serializers


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