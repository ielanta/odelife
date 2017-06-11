from django.conf.urls import url, include
from accounts.forms import ExtRegistrationForm
from registration.backends.default.views import RegistrationView

urlpatterns = [
    url(r'^register/$', RegistrationView.as_view(form_class=ExtRegistrationForm), name='registration_register'),
    url('', include('registration.backends.default.urls')),
]

