from django.shortcuts import render

from rest_framework import generics
from .serializers import AromaListSerializer
from aroma.models import Aroma


class AromaList(generics.ListCreateAPIView):
    queryset = Aroma.objects.filter(is_public = True)
    serializer_class = AromaListSerializer
