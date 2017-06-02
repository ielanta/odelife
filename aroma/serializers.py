from django import forms
from django.core.exceptions import ValidationError
from django.db.models import Q

from dal import autocomplete
from django_filters.rest_framework import NumberFilter, FilterSet, MultipleChoiceFilter, CharFilter, \
    ModelMultipleChoiceFilter, ModelChoiceFilter
from rest_framework import serializers

from aroma.models import Aroma, Brand, Note, Group, Nose, CategoryNotes
from core.settings import GENDER_CHOICES


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
        fields = ('id', 'title', 'year', 'brand', 'pic', 'group')


class NoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Note
        fields = '__all__'


class BrandSerializer(serializers.ModelSerializer):
    class Meta:
        model = Brand
        fields = ('id', 'title', 'logo')


class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = '__all__'


class NoseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Nose
        fields = ('id', 'name')


class AromaDetailSerializer(serializers.ModelSerializer):
    top_notes = serializers.SerializerMethodField()
    middle_notes = serializers.SerializerMethodField()
    base_notes = serializers.SerializerMethodField()
    general_notes = serializers.SerializerMethodField()
    noses = NoseSerializer(read_only=True, many=True)
    gender_label = serializers.SerializerMethodField()
    brand = BrandSerializer(read_only=True)
    group = GroupSerializer(read_only=True)

    @staticmethod
    def get_gender_label(obj):
        return obj.get_gender_display()

    @staticmethod
    def get_top_notes(obj):
        notes = obj.notes.filter(categorynotes__category=CategoryNotes.TOP_NOTES).all()
        return NoteSerializer(notes, many=True, read_only=True).data

    @staticmethod
    def get_middle_notes(obj):
        notes = obj.notes.filter(categorynotes__category=CategoryNotes.MIDDLE_NOTES).all()
        return NoteSerializer(notes, many=True, read_only=True).data

    @staticmethod
    def get_base_notes(obj):
        notes = obj.notes.filter(categorynotes__category=CategoryNotes.BASE_NOTES).all()
        return NoteSerializer(notes, many=True, read_only=True).data

    @staticmethod
    def get_general_notes(obj):
        notes = obj.notes.filter(categorynotes__category=CategoryNotes.GENERAL_NOTES).all()
        return NoteSerializer(notes, many=True, read_only=True).data

    class Meta:
        model = Aroma
        fields = ('id', 'title', 'year', 'brand', 'pic', 'group', 'gender', 'gender_label', 'noses', 'description',
                  'top_notes', 'middle_notes', 'base_notes', 'general_notes')
