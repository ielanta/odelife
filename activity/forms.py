from django import forms

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Field, Submit

from activity.models import Comment


class CommentCreateForm(forms.ModelForm):
    text = forms.CharField(label="Комментарий", max_length=1000, widget=forms.Textarea(attrs={'autofocus': True}))
    impression = forms.ChoiceField(choices=Comment.IMPRESSION_TYPES, label="Впечатление", widget=forms.RadioSelect)
    longevity = forms.ChoiceField(choices=Comment.LONGEVITY_TYPES, label="Стойкость", required=False,
                                  widget=forms.RadioSelect)
    sillage = forms.ChoiceField(choices=Comment.SILLAGE_TYPES, label="Шлейф", required=False, widget=forms.RadioSelect)
    season = forms.ChoiceField(choices=Comment.SEASON_TYPES, label="Время года", required=False,
                               widget=forms.RadioSelect)

    def __init__(self, *args, **kwargs):
        super(CommentCreateForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.layout = Layout('text',
                                    Field('impression', template='radio_button.html'),
                                    Field('longevity', template='radio_button.html'),
                                    Field('sillage', template='radio_button.html'),
                                    Field('season', template='radio_button.html'),)
        self.helper.layout.append(Submit('save', 'Отправить', css_class='btn btn-base center-block'))

    class Meta:
        model = Comment
        fields = ('text', 'impression', 'longevity', 'sillage', 'season')
