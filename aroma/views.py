from django.db.models import Q
from django.shortcuts import redirect, render
from django.core.urlresolvers import reverse
from dal import autocomplete
from django.views.generic.edit import FormView
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics
from rest_framework.filters import OrderingFilter
from rest_framework.renderers import TemplateHTMLRenderer
from aroma.serializers import AromaListSerializer, SearchFilter, AromaDetailSerializer
from aroma.forms import AromaSearchForm, AromaCompactSearchForm, NoteCompactSearchForm
from aroma.models import Aroma, Brand, Note, Group, Nose
from main.pagination import CustomPagination
from main.permissions import PublicEndpoint


class AromaList(generics.ListCreateAPIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'search.html'
    serializer_class = AromaListSerializer
    pagination_class = CustomPagination
    allowed_methods = ['GET']
    filter_backends = (DjangoFilterBackend, OrderingFilter)
    filter_class = SearchFilter
    queryset = Aroma.objects.filter(is_public=True)
    permission_classes = (PublicEndpoint,)
    ordering_fields = ('year', 'aromacounter__num_comments', 'title', 'updated_at')
    ordering = ('-year', 'title')

    def list(self, request, *args, **kwargs):
        response = super(AromaList, self).list(request, format='json', *args, **kwargs)
        form = AromaSearchForm(data=request.query_params)

        if not form.is_valid():
            try:
                render(request, self.template_name, {'form': form})
            except ValueError:
                # TODO: Logger
                form = AromaSearchForm()

        response.data['form'] = form
        return response


class AromaDetail(generics.RetrieveAPIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'item.html'
    serializer_class = AromaDetailSerializer
    allowed_methods = ['GET']
    queryset = Aroma.objects.filter(is_public=True).all()
    permission_classes = (PublicEndpoint,)
    lookup_field = 'slug'


class BrandAutocomplete(autocomplete.Select2QuerySetView):
    def get_queryset(self):
        qs = Brand.objects.filter(aroma__is_public=True).distinct('title').order_by('title').all()
        if self.q:
            qs = qs.filter(title__istartswith=self.q)
        return qs


class NotesAutocomplete(autocomplete.Select2QuerySetView):
    def get_queryset(self):
        qs = Note.objects.exclude(pic='').order_by('title').all()
        if self.q:
            qs = qs.filter(Q(title__istartswith=self.q.capitalize()) | Q(title__icontains=self.q))
        return qs


class GroupsAutocomplete(autocomplete.Select2QuerySetView):
    def get_queryset(self):
        qs = Group.objects.all().order_by('title')
        if self.q:
            qs = qs.filter(title__istartswith=self.q.lower())
        return qs


class NosesAutocomplete(autocomplete.Select2QuerySetView):
    def get_queryset(self):
        qs = Nose.objects.filter(aroma__is_public=True).distinct('name').order_by('name').all()
        if self.q:
            qs = qs.filter(Q(name__istartswith=self.q.capitalize()) | Q(name__icontains=self.q))
        return qs


class AromaCompactSearch(FormView):
    form_class = AromaCompactSearchForm
    template_name = 'home.html'

    def get(self, request, *args, **kwargs):
        form = self.form_class(request.GET)
        if form.data and form.is_valid():
            return redirect(reverse('aroma-list') + '?title=%s' % form.data.get('title'))
        return render(request, self.template_name, {'form': form})


class NoteCompactSearch(FormView):
    form_class = NoteCompactSearchForm
    template_name = 'search_notes.html'

    def get(self, request, *args, **kwargs):
        form = self.form_class(request.GET)
        if form.data and form.is_valid():
            return redirect(reverse('aroma-list') + '?' + request.GET.urlencode())
        else:
            try:
                return render(request, self.template_name, {'form': form})
            except ValueError:
                # TODO: Logger
                form = self.form_class()
                return render(request, self.template_name, {'form': form})

