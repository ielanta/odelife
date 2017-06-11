from django import forms
from django.core.urlresolvers import reverse

from registration.forms import RegistrationFormUniqueEmail


class ExtRegistrationForm(RegistrationFormUniqueEmail):
    def __init__(self, *args, **kwargs):
        super(ExtRegistrationForm, self).__init__(*args, **kwargs)
        self.fields['username'].help_text = ''
        self.fields['password2'].label = 'Повторите пароль, чтобы не ошибиться'
        self.fields['password2'].help_text = ''

    # def __init__(self, *args, **kwargs):
    #     from crispy_forms.helper import FormHelper
    #     from crispy_forms.layout import Layout, Field
    #
    #     super(ExtRegistrationForm, self).__init__(*args, **kwargs)
    #     self.helper = FormHelper()
    #     self.helper.layout = Layout(Field('tos', template='checkbox_helper.html'))