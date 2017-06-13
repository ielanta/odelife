from django.shortcuts import redirect
from django.core.urlresolvers import reverse_lazy
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.views import PasswordResetView


from registration.backends.default.views import RegistrationView, ActivationView, ResendActivationView


class ExtRegistrationView(SuccessMessageMixin, RegistrationView):
    success_message = 'Письмо со ссылкой для активации было успешно отправлено'
    success_url = 'registration_register'


class ExtActivationView(ActivationView):
    def get_success_url(self, user):
        return reverse_lazy('aroma-list')


class ExtResendActivationView(SuccessMessageMixin, ResendActivationView):
    success_message = 'Письмо со ссылкой для активации было успешно отправлено'

    def render_form_submitted_template(self, form):
        return redirect(reverse_lazy('registration_resend_activation'))


class ExtPasswordResetView(SuccessMessageMixin, PasswordResetView):
    success_message = 'Письмо со ссылкой для смены пароля было успешно отправлено'
    success_url = reverse_lazy('auth_password_reset')
    html_email_template_name = 'registration/password_reset_email.html'
