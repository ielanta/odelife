from django.conf.urls import url, include
from django.contrib.auth.views import LoginView
from accounts.forms import ExtRegistrationForm, EmailAuthenticationForm
from accounts.views import ExtRegistrationView, ExtActivationView, ExtResendActivationView, ExtPasswordResetView, \
    ExtPasswordResetConfirmView, FavoritesPost

urlpatterns = [
    url(r'^register/$', ExtRegistrationView.as_view(form_class=ExtRegistrationForm), name='registration_register'),
    url(r'^login/$', LoginView.as_view(template_name='registration/login.html', form_class=EmailAuthenticationForm),
        name='auth_login'),
    url(r'^activate/resend/$', ExtResendActivationView.as_view(), name='registration_resend_activation'),
    url(r'^activate/(?P<activation_key>\w+)/$', ExtActivationView.as_view(), name='registration_activate'),
    url(r'^password/reset/confirm/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>.+)/$',
        ExtPasswordResetConfirmView.as_view(), name='auth_password_reset_confirm'),
    url(r'^password/reset/$', ExtPasswordResetView.as_view(), name='auth_password_reset'),
    url(r'', include('social_django.urls', namespace='social')),
    url(r'^', include('registration.backends.default.urls')),
    url(r'^me/favorites/(?P<aroma_id>[0-9]+)/$', FavoritesPost.as_view(), name='add-favorite'),
]
