from django.core.urlresolvers import reverse_lazy
from django.contrib.messages.views import SuccessMessageMixin

from registration.backends.simple.views import RegistrationView


class ExtRegistrationView(SuccessMessageMixin, RegistrationView):
    success_message = 'Письмо со ссылкой для активации было успешно отправлено'

    def get_success_url(self, user):
        return reverse_lazy('registration_register')
