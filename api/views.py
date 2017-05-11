from django_filters.rest_framework import DjangoFilterBackend

from rest_framework import generics
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.response import Response
from .serializers import AromaListSerializer
from aroma.models import Aroma


class AromaList(generics.ListCreateAPIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'search.html'
    serializer_class = AromaListSerializer
    allowed_methods = ['GET']
    filter_backends = (DjangoFilterBackend,)
    filter_fields = ('gender', 'year')
    queryset = Aroma.objects.filter(is_public=True)

    def list(self, request, *args, **kwargs):
        response = super(AromaList, self).list(request, format='json', *args, **kwargs)
        serializer = AromaListSerializer(data=request.query_params)
        if not serializer.is_valid():
            serializer = AromaListSerializer()
        return Response({'items': response.data['results'], 'serializer': serializer})
