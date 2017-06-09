from django.conf import settings
from django.shortcuts import render


def tos(request):
    return render(request, 'tos.html')


def contacts(request):
    context = {'mail_service': settings.MAIL_SERVICE, 'mail_marketing': settings.MAIL_MARKETING}
    return render(request, 'contacts.html', context)
