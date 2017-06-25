from django.core.mail import send_mail
from django.contrib.messages.views import SuccessMessageMixin
from django.shortcuts import render
from django.views.generic.edit import FormView
from django.core.urlresolvers import reverse_lazy
from django.template import loader

from main.forms import ContactForm


def tos(request):
    return render(request, 'tos.html')


class ContactView(SuccessMessageMixin, FormView):
    form_class = ContactForm
    template_name = 'contact/contact_form.html'
    success_message = 'Ваше обращение было успешно отправлено'
    success_url = reverse_lazy('contacts')

    def post(self, request, *args, **kwargs):
        form = self.form_class(data=request.POST)
        if form.is_valid():
            html_message = loader.render_to_string(form.html_email_template_name, self.get_context_data())
            send_mail(form.subject, request.POST.get('msg'), form.from_email, [form.to_email],
                      html_message=html_message)
        return super(ContactView, self).post(request, *args, **kwargs)
