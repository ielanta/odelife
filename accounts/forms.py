from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UsernameField, AuthenticationForm
from django.core.exceptions import ValidationError, ObjectDoesNotExist
from registration.forms import RegistrationFormUniqueEmail


class ExtRegistrationForm(RegistrationFormUniqueEmail):
    username = UsernameField(max_length=254, min_length=6, widget=forms.TextInput(attrs={'autofocus': True}))

    def __init__(self, *args, **kwargs):
        super(ExtRegistrationForm, self).__init__(*args, **kwargs)
        self.fields['username'].help_text = ''
        self.fields['password2'].label = 'Повторите пароль, чтобы не ошибиться'
        self.fields['password1'].help_text = ''
        self.fields['password2'].help_text = ''


class EmailAuthenticationForm(AuthenticationForm):
    def clean_username(self):
        username = self.data['username']
        if '@' in username:
            try:
                username = User.objects.get(email=username).username
            except ObjectDoesNotExist:
                raise ValidationError(
                    self.error_messages['invalid_login'],
                    code='invalid_login',
                    params={'username': self.username_field.verbose_name},
                )
        return username

    def __init__(self, *args, **kwargs):
        super(EmailAuthenticationForm, self).__init__(*args, **kwargs)
        self.fields['username'].label = 'E-mail или Имя пользователя'
