from django.conf.urls import url, include
from accounts.forms import ExtRegistrationForm
from accounts.views import ExtRegistrationView

urlpatterns = [
    url(r'^register/$', ExtRegistrationView.as_view(form_class=ExtRegistrationForm), name='registration_register'),
    url('', include('registration.backends.default.urls')),
]

