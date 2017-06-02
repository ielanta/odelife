from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics
from rest_framework.filters import OrderingFilter
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.response import Response
from .serializers import AromaListSerializer, SearchFilter, AromaSearchForm, AromaDetailSerializer
from aroma.models import Aroma
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
    ordering_fields = ('title', 'year', 'aromacounter__num_comments')
    ordering = ('-year',)

    def list(self, request, *args, **kwargs):
        response = super(AromaList, self).list(request, format='json', *args, **kwargs)
        form = AromaSearchForm(data=request.query_params)
        return Response({'data': response.data, 'form': form})


class AromaDetail(generics.RetrieveAPIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'item.html'
    serializer_class = AromaDetailSerializer
    allowed_methods = ['GET']
    queryset = Aroma.objects.filter(is_public=True).all()
    permission_classes = (PublicEndpoint,)