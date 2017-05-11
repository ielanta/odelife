from rest_framework import serializers
from aroma.models import Aroma
from core.settings import GENDER_CHOICES


class AromaListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Aroma
        fields = ('id', 'title', 'year', 'gender')

    year = serializers.IntegerField(label="Год", required=False)
    title = serializers.CharField(label="Название", required=False)
    gender = serializers.ChoiceField(choices=GENDER_CHOICES, label="Пол", required=False)

