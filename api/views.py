from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.filters import OrderingFilter
from rest_framework.permissions import IsAuthenticated
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.response import Response
from .serializers import AromaListSerializer, SearchFilter, AromaSearchForm
from aroma.models import Aroma


class AromaList(generics.ListCreateAPIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'search.html'
    serializer_class = AromaListSerializer
    allowed_methods = ['GET']
    filter_backends = (DjangoFilterBackend, OrderingFilter)
    filter_class = SearchFilter
    queryset = Aroma.objects.filter(is_public=True)
    authentication_classes = (SessionAuthentication, BasicAuthentication)
    permission_classes = (IsAuthenticated,)
    ordering_fields = ('title', 'year', 'aromacounter__num_comments')
    ordering = ('-year',)

    def list(self, request, *args, **kwargs):
        response = super(AromaList, self).list(request, format='json', *args, **kwargs)
        form = AromaSearchForm(data=request.query_params)
        return Response({'items': response.data['results'], 'form': form})
