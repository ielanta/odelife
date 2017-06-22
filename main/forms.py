from django import forms
from core.settings import DEFAULT_FROM_EMAIL, MAIL_SERVICE


class ContactForm(forms.Form):
    email = forms.EmailField(label='Ваш Email', max_length=200)
    msg = forms.CharField(label='Чем мы можем вам помочь?', widget=forms.Textarea)
    from_email = DEFAULT_FROM_EMAIL
    to_email = MAIL_SERVICE
    html_email_template_name = 'contact_form/contact_form_email.html'
    subject = ''
