from django.conf.urls import url, include
from accounts.forms import ExtRegistrationForm
from accounts.views import ExtRegistrationView, ExtActivationView, ExtResendActivationView, ExtPasswordResetView

urlpatterns = [
    url(r'^register/$', ExtRegistrationView.as_view(form_class=ExtRegistrationForm), name='registration_register'),
    url(r'^activate/resend/$', ExtResendActivationView.as_view(), name='registration_resend_activation'),
    url(r'^activate/(?P<activation_key>\w+)/$', ExtActivationView.as_view(), name='registration_activate'),
    url(r'^password/reset/$', ExtPasswordResetView.as_view(), name='auth_password_reset'),
    url(r'^', include('registration.backends.default.urls')),
]

