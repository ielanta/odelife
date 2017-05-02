from django.shortcuts import render
from .models import Aroma


def get_aroma(request, id):
    fr = Aroma.objects.get(id=id)
    return render(request, 'item.html', {'item': fr})
