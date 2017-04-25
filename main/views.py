from django.conf import settings
from django.shortcuts import render


def home(request):
    return render(request, 'home.html')


def contacts(request):
    context = {'mail_service': settings.MAIL_SERVICE, 'mail_marketing': settings.MAIL_MARKETING}
    return render(request, 'contacts.html', context)
