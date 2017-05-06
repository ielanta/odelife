from rest_framework import serializers
from aroma.models import Aroma


class AromaListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Aroma
        fields = ('id', 'title', 'year', 'brand')