from django import forms
from dal import autocomplete
from django_filters.rest_framework import NumberFilter, FilterSet, MultipleChoiceFilter, CharFilter
from rest_framework import serializers
from aroma.models import Aroma, Brand
from core.settings import GENDER_CHOICES


class SearchFilter(FilterSet):
    min_year = NumberFilter(name="year", lookup_expr='gte')
    max_year = NumberFilter(name="year", lookup_expr='lte')
    title = CharFilter(name="title", lookup_expr='contains')
    gender = MultipleChoiceFilter(choices=GENDER_CHOICES,
                                  method=lambda queryset, name, value: queryset.filter(gender__in=value))

    class Meta:
        model = Aroma
        fields = ['gender', 'min_year', 'max_year', 'title', 'brand']


class AromaSearchForm(forms.Form):
    class Meta:
        model = Aroma
        fields = ('id', 'title', 'gender', 'min_year', 'max_year', 'brand')

    title = forms.CharField(label="Название", required=False, max_length=200)
    gender = forms.MultipleChoiceField(choices=GENDER_CHOICES, label="Пол", required=False,
                                       widget=forms.CheckboxSelectMultiple)
    min_year = forms.IntegerField(label="Год выпука", required=False, min_value=1700, max_value=2100,
                                  widget=forms.NumberInput(attrs={'placeholder': 'с'}))
    max_year = forms.IntegerField(label=" ", required=False, min_value=1700, max_value=2100,
                                  widget=forms.NumberInput(attrs={'placeholder': 'по'}))
    brand = forms.ModelChoiceField(label='Дизайнер',
        queryset=Brand.objects.all(), required=False,
        widget=autocomplete.ModelSelect2(url='brand-autocomplete')
    )


class AromaListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Aroma
        fields = ('id', 'title', 'gender', 'year', 'brand')
