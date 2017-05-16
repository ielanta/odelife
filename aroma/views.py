from django.shortcuts import render
from dal import autocomplete
from .models import Aroma, Brand, Note, Group, Nose


def get_aroma(request, id):
    fr = Aroma.objects.get(id=id)
    return render(request, 'item.html', {'item': fr})


class BrandAutocomplete(autocomplete.Select2QuerySetView):
    def get_queryset(self):
        qs = Brand.objects.filter(aroma__is_public=True).all()
        if self.q:
            qs = qs.filter(title__istartswith=self.q)
        return qs


class NotesAutocomplete(autocomplete.Select2QuerySetView):
    def get_queryset(self):
        qs = Note.objects.all().order_by('title')
        if self.q:
            qs = qs.filter(title__istartswith=self.q.capitalize())
        return qs


class GroupAutocomplete(autocomplete.Select2QuerySetView):
    def get_queryset(self):
        qs = Group.objects.all().order_by('title')
        if self.q:
            qs = qs.filter(title__istartswith=self.q.lower())
        return qs


class NosesAutocomplete(autocomplete.Select2QuerySetView):
    def get_queryset(self):
        qs = Nose.objects.filter(aroma__is_public=True).all().order_by('name')
        if self.q:
            qs = qs.filter(name__istartswith=self.q.capitalize())
        return qs
