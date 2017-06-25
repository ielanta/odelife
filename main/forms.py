from django import forms
from django.conf import settings


class ContactForm(forms.Form):
    email = forms.EmailField(label='Ваш E-mail', max_length=200)
    msg = forms.CharField(label='Чем мы можем вам помочь?', widget=forms.Textarea)
    from_email = settings.DEFAULT_FROM_EMAIL
    to_email = settings.MAIL_SERVICE
    html_email_template_name = 'contact/contact_email.html'
    subject = ''
