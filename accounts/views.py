from django.contrib.auth.views import PasswordResetView, PasswordResetConfirmView, PasswordChangeView
from django.contrib.auth.models import User
from django.contrib.messages.views import SuccessMessageMixin
from django.core.urlresolvers import reverse_lazy
from django.shortcuts import get_object_or_404, redirect
from registration.backends.default.views import RegistrationView, ActivationView, ResendActivationView
from django.views.generic.edit import UpdateView
from rest_framework.generics import ListAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.renderers import TemplateHTMLRenderer
from main.pagination import CustomPagination
from main.permissions import PublicEndpoint


from accounts.forms import ProfileForm
from activity. models import Activity, Comment
from activity.serializers import AromaCommentSerializer
from aroma.models import Aroma
from aroma.serializers import AromaListSerializer


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
    template_name = 'profile_settings_form.html'
    form_class = ProfileForm
    success_message = 'Данные профиля успешно обновлены'

    def get_object(self, queryset=None):
        return self.request.user

    def get_success_url(self):
        return self.request.META.get('HTTP_REFERER')


class MyFavoritesView(ListAPIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'profile/profile_favorites.html'
    serializer_class = AromaListSerializer
    pagination_class = CustomPagination
    allowed_methods = ['GET']
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        return Aroma.objects.filter(marks__user_id=self.request.user, marks__activity_type=Activity.FAVORITE)\
            .order_by('-marks__created_at')


class MyLikesView(MyFavoritesView):
    def get_queryset(self):
        return Aroma.objects.filter(marks__user_id=self.request.user, marks__activity_type=Activity.LIKE)\
            .order_by('-marks__created_at')


class MyCommentsView(ListAPIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'profile/profile_comments.html'
    serializer_class = AromaCommentSerializer
    pagination_class = CustomPagination
    allowed_methods = ['GET']
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        return Comment.objects.filter(user_id=self.request.user).order_by('-created_at')


class PublicCommentsView(MyCommentsView):
    template_name = 'profile/profile_public.html'
    permission_classes = (PublicEndpoint,)

    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs['username'])
        return Comment.objects.filter(user_id=user.id).order_by('-created_at')

    def get(self, request, *args, **kwargs):
        user = get_object_or_404(User, username=self.kwargs['username'])
        request.GET.full_username = user.account.get_full_name()
        return super(PublicCommentsView, self).get(request, *args, **kwargs)


