from django.forms.widgets import CheckboxSelectMultiple, RadioSelect
from django.forms import widgets
from django import forms
from rest_framework import serializers
from aroma.models import Aroma
from core.settings import GENDER_CHOICES


class AromaListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Aroma
        fields = ('id', 'title', 'gender', 'min_year', 'max_year', 'brand')

    min_year = serializers.IntegerField(label="Год(c)", required=False, default=None)
    max_year = serializers.IntegerField(label="Год(по)", required=False, default=None)
    title = serializers.CharField(label="Название", required=False)
    gender = serializers.MultipleChoiceField(choices=GENDER_CHOICES, label="Пол", required=False)
    #brand = serializers.CharField(label="Дизайнер")

