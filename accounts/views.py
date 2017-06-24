from django.contrib.auth.views import PasswordResetView, PasswordResetConfirmView, PasswordChangeView
from django.contrib.auth.models import User
from django.contrib.messages.views import SuccessMessageMixin
from django.core.urlresolvers import reverse_lazy
from django.shortcuts import redirect
from registration.backends.default.views import RegistrationView, ActivationView, ResendActivationView
from django.views.generic.edit import UpdateView

from .forms import ProfileForm


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
    success_message = 'Если аккаунт с таким адресом существует, вы получите ссылку для смены пароля'
    success_url = reverse_lazy('auth_password_reset')
    html_email_template_name = 'registration/password_reset_email.html'


class ExtPasswordResetConfirmView(SuccessMessageMixin, PasswordResetConfirmView):
    success_message = 'Пароль успешно изменен'
    success_url = reverse_lazy('auth_login')


class ExtPasswordChangeView(SuccessMessageMixin, PasswordChangeView):
    success_message = 'Пароль успешно изменен'
    success_url = reverse_lazy('auth_password_change')


class ProfileView(SuccessMessageMixin, UpdateView):
    model = User
    template_name = 'profile.html'
    form_class = ProfileForm
    success_message = 'Данные профиля успешно обновлены'

    def get_object(self, queryset=None):
        return self.request.user

    def get_success_url(self):
        return self.request.META.get('HTTP_REFERER')
