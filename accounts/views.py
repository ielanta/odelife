from django.shortcuts import redirect, get_object_or_404
from django.core.urlresolvers import reverse_lazy
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.views import PasswordResetView, PasswordResetConfirmView

from registration.backends.default.views import RegistrationView, ActivationView, ResendActivationView
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

from aroma.models import Aroma
from accounts.models import Activity


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


class ActivityCreate(generics.CreateAPIView):
    permission_classes = (IsAuthenticated,)
    activity_type = ''

    def post(self, request, *args, **kwargs):
        aroma = get_object_or_404(Aroma, id=kwargs.get('aroma_id'))
        aroma.marks.get_or_create(activity_type=self.activity_type, user=request.user)
        return redirect(request.META.get('HTTP_REFERER'))


class ActivityDelete(generics.DestroyAPIView):
    permission_classes = (IsAuthenticated,)
    activity_type = ''

    def get(self, request, *args, **kwargs):
        Activity.objects.get(pk=kwargs.get('pk')).delete()
        return redirect(request.META.get('HTTP_REFERER'))
