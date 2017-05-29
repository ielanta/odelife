from django import forms
from dal import autocomplete
from django_filters.rest_framework import NumberFilter, FilterSet, MultipleChoiceFilter, CharFilter, \
    ModelMultipleChoiceFilter, ModelChoiceFilter

from django.db.models import Q
from rest_framework import serializers
from aroma.models import Aroma, Brand, Note, Group, Nose
from core.settings import GENDER_CHOICES
from django.core.exceptions import ValidationError

LIMIT_NOTES = 10


class SearchFilter(FilterSet):
    min_year = NumberFilter(name="year", lookup_expr='gte')
    max_year = NumberFilter(name="year", lookup_expr='lte')
    title = CharFilter(name="title", lookup_expr='contains')
    gender = MultipleChoiceFilter(choices=GENDER_CHOICES,
                                  method=lambda queryset, name, value: queryset.filter(gender__in=value))
    notes = ModelMultipleChoiceFilter(queryset=Note.objects.all(), conjoined=True)
    group = ModelChoiceFilter(queryset=Group.objects.all(), method=lambda queryset, name, value: queryset.filter(
        Q(group=value) | Q(group__parent=value)))
    noses = ModelMultipleChoiceFilter(name="noses", queryset=Nose.objects.all(), conjoined=True)

    class Meta:
        model = Aroma
        fields = ('gender', 'min_year', 'max_year', 'title', 'brand', 'notes', 'notes', 'group', 'noses')


class AromaSearchForm(forms.Form):
    class Meta:
        model = Aroma
        fields = ('id', 'title', 'gender', 'min_year', 'max_year', 'brand', 'notes', 'group', 'noses')

    title = forms.CharField(label="Название", required=False, max_length=200)
    gender = forms.MultipleChoiceField(choices=GENDER_CHOICES, label="Пол", required=False,
                                       widget=forms.CheckboxSelectMultiple)
    min_year = forms.IntegerField(label="Год", required=False, min_value=1700, max_value=2100,
                                  widget=forms.NumberInput(attrs={'placeholder': 'с'}))
    max_year = forms.IntegerField(label=" ", required=False, min_value=1700, max_value=2100,
                                  widget=forms.NumberInput(attrs={'placeholder': 'по'}))
    group = forms.ModelChoiceField(label='Группа', queryset=Group.objects.all(), required=False,
                                   widget=autocomplete.ModelSelect2(url='group-autocomplete'))
    brand = forms.ModelChoiceField(label='Бренд', queryset=Brand.objects.all(), required=False,
                                   widget=autocomplete.ModelSelect2(url='brand-autocomplete'))
    notes = forms.ModelMultipleChoiceField(label='Ноты', queryset=Note.objects.all(), required=False,
                                           widget=autocomplete.ModelSelect2Multiple(url='notes-autocomplete'))
    noses = forms.ModelMultipleChoiceField(label='Парфюмеры', queryset=Nose.objects.all(), required=False,
                                           widget=autocomplete.ModelSelect2Multiple(url='noses-autocomplete'))

    def clean_notes(self):
        data = self.cleaned_data['notes']
        if len(data) > LIMIT_NOTES:
            raise ValidationError("Максимальное число нот для поиска: %d" % LIMIT_NOTES)
        return data


class AromaListSerializer(serializers.ModelSerializer):
    group = serializers.SlugRelatedField(read_only=True, slug_field='title')
    brand = serializers.SlugRelatedField(read_only=True, slug_field='title')

    class Meta:
        model = Aroma
        fields = ('id', 'title', 'gender', 'year', 'brand', 'pic', 'group')
