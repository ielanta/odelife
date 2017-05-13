from django.shortcuts import render
from dal import autocomplete
from .models import Aroma, Brand


def get_aroma(request, id):
    fr = Aroma.objects.get(id=id)
    return render(request, 'item.html', {'item': fr})


class BrandAutocomplete(autocomplete.Select2QuerySetView):
    def get_queryset(self):
        qs = Brand.objects.filter(aroma__is_public=True).all()
        if self.q:
            qs = qs.filter(title__istartswith=self.q)
        return qs
