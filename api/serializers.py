from django import forms
from django_filters.rest_framework import NumberFilter, FilterSet, MultipleChoiceFilter, CharFilter
from rest_framework import serializers
from aroma.models import Aroma
from core.settings import GENDER_CHOICES


class SearchFilter(FilterSet):
    min_year = NumberFilter(name="year", lookup_expr='gte')
    max_year = NumberFilter(name="year", lookup_expr='lte')
    title = CharFilter(name="title", lookup_expr='contains')
    gender = MultipleChoiceFilter(choices=GENDER_CHOICES,
                                  method=lambda queryset, name, value: queryset.filter(gender__in=value))

    class Meta:
        model = Aroma
        fields = ['gender', 'min_year', 'max_year', 'title']


class AromaSearchForm(forms.Form):
    class Meta:
        model = Aroma
        fields = ('id', 'title', 'gender', 'min_year', 'max_year', 'brand')
    title = forms.CharField(label="Название", required=False)
    gender = forms.MultipleChoiceField(choices=GENDER_CHOICES, label="Пол", required=False,
                                       widget=forms.CheckboxSelectMultiple)
    min_year = forms.IntegerField(label="Год(c)", required=False)
    max_year = forms.IntegerField(label="Год(по)", required=False)


class AromaListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Aroma
        fields = ('id', 'title', 'gender', 'year', 'brand')