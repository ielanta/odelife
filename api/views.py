from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.response import Response
from .serializers import AromaListSerializer, SearchFilter, AromaSearchForm
from aroma.models import Aroma


class AromaList(generics.ListCreateAPIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'search.html'
    serializer_class = AromaListSerializer
    allowed_methods = ['GET']
    filter_backends = (DjangoFilterBackend,)
    filter_class = SearchFilter
    queryset = Aroma.objects.filter(is_public=True)

    def list(self, request, *args, **kwargs):
        response = super(AromaList, self).list(request, format='json', *args, **kwargs)
        form = AromaSearchForm(data=request.query_params)
        return Response({'items': response.data['results'], 'form': form})
