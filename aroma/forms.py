from django import forms
from django.core.exceptions import ValidationError

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Field
from dal import autocomplete

from aroma.models import Aroma, Brand, Note, Group, Nose
from core.settings import GENDER_CHOICES

LIMIT_NOTES = 10


class AromaSearchForm(forms.Form):
    class Meta:
        model = Aroma
        fields = ('title', 'gender', 'min_year', 'max_year', 'brand', 'notes', 'groups', 'noses')

    title = forms.CharField(label="Название", required=False, max_length=200)
    gender = forms.MultipleChoiceField(choices=GENDER_CHOICES, label="Пол", required=False,
                                       widget=forms.CheckboxSelectMultiple)
    min_year = forms.IntegerField(label="Год", required=False, min_value=1700, max_value=2100,
                                  widget=forms.NumberInput(attrs={'placeholder': 'с'}))
    max_year = forms.IntegerField(label=" ", required=False, min_value=1700, max_value=2100,
                                  widget=forms.NumberInput(attrs={'placeholder': 'по'}))
    groups = forms.ModelMultipleChoiceField(label='Группа', queryset=Group.objects.all(), required=False,
                                            widget=autocomplete.ModelSelect2Multiple(url='groups-autocomplete'))
    brand = forms.ModelChoiceField(label='Бренд', queryset=Brand.objects.all(), required=False,
                                   widget=autocomplete.ModelSelect2(url='brand-autocomplete'))
    notes = forms.ModelMultipleChoiceField(label='Ноты', queryset=Note.objects.all(), required=False,
                                           widget=autocomplete.ModelSelect2Multiple(url='notes-autocomplete'))
    noses = forms.ModelMultipleChoiceField(label='Парфюмеры', queryset=Nose.objects.all(), required=False,
                                           widget=autocomplete.ModelSelect2Multiple(url='noses-autocomplete'))

    def __init__(self, *args, **kwargs):
        super(AromaSearchForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout('title', Field('gender', template='checkbox_helper.html'))

    def clean_notes(self):
        data = self.cleaned_data['notes']
        if len(data) > LIMIT_NOTES:
            raise ValidationError("Максимальное число нот для поиска: %d" % LIMIT_NOTES)
        return data


class AromaCompactSearchForm(forms.ModelForm):
    class Meta:
        model = Aroma
        fields = ('title',)

    title = forms.CharField(label="", required=False, max_length=200,
                            widget=forms.TextInput(
                                attrs={'placeholder': 'Название парфюма', 'itemprop': 'query-input'}))
