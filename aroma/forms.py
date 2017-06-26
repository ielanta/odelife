from django import forms

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Field, Submit
from dal import autocomplete

from aroma.models import Aroma, Brand, Note, Group, Nose
from aroma.validators import validate_notes
from django.conf import settings


class AromaSearchForm(forms.Form):
    class Meta:
        model = Aroma
        fields = ('title', 'gender', 'min_year', 'max_year', 'brand', 'in_notes', 'ex_notes', 'groups', 'noses')

    title = forms.CharField(label="Название", required=False, max_length=200)
    gender = forms.MultipleChoiceField(choices=settings.GENDER_CHOICES, label="Пол", required=False,
                                       widget=forms.CheckboxSelectMultiple)
    min_year = forms.IntegerField(label="Год", required=False, min_value=1700, max_value=2100,
                                  widget=forms.NumberInput(attrs={'placeholder': 'с'}))
    max_year = forms.IntegerField(label=" ", required=False, min_value=1700, max_value=2100,
                                  widget=forms.NumberInput(attrs={'placeholder': 'по'}))
    groups = forms.ModelMultipleChoiceField(label='Группа', queryset=Group.objects.all(), required=False,
                                            widget=autocomplete.ModelSelect2Multiple(url='groups-autocomplete'))
    brand = forms.ModelChoiceField(label='Бренд', queryset=Brand.objects.all(), required=False,
                                   widget=autocomplete.ModelSelect2(url='brand-autocomplete'))
    in_notes = forms.ModelMultipleChoiceField(label='Включить ноты', queryset=Note.objects.all(), required=False,
                                              validators=[validate_notes],
                                              widget=autocomplete.ModelSelect2Multiple(url='notes-autocomplete'))
    ex_notes = forms.ModelMultipleChoiceField(label='Исключить ноты', queryset=Note.objects.all(), required=False,
                                              validators=[validate_notes],
                                              widget=autocomplete.ModelSelect2Multiple(url='notes-autocomplete'))
    noses = forms.ModelMultipleChoiceField(label='Парфюмеры', queryset=Nose.objects.all(), required=False,
                                           widget=autocomplete.ModelSelect2Multiple(url='noses-autocomplete'))

    def __init__(self, *args, **kwargs):
        super(AromaSearchForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout('title', Field('gender', template='checkbox_helper.html'))


class AromaCompactSearchForm(forms.ModelForm):
    class Meta:
        model = Aroma
        fields = ('title',)

    title = forms.CharField(label="", required=False, max_length=200,
                            widget=forms.TextInput(attrs={'placeholder': 'Название парфюма', 'itemprop': 'query-input',
                                                          'autofocus': True}))


class NoteCompactSearchForm(forms.Form):
    in_notes = forms.ModelMultipleChoiceField(label='Включить ноты', queryset=Note.objects.all(), required=False,
                                              validators=[validate_notes],
                                              widget=autocomplete.ModelSelect2Multiple(url='notes-autocomplete'))
    ex_notes = forms.ModelMultipleChoiceField(label='Исключить ноты', queryset=Note.objects.all(), required=False,
                                              validators=[validate_notes],
                                              widget=autocomplete.ModelSelect2Multiple(url='notes-autocomplete'))

    class Meta:
        model = Aroma
        fields = ('in_notes', 'ex_notes')

    def __init__(self, *args, **kwargs):
        super(NoteCompactSearchForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.layout.append(Submit('submit', 'Найти', css_class='btn btn-base center-block'))
