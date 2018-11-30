from django.shortcuts import render
from rest_framework import generics
from .serializers import ComunidadSerializers
from core.models import Comunidad

# Create your views here.

class ComunidadLista(generics.ListCreateAPIView):
    queryset = Comunidad.objects.all()
    serializer_class = ComunidadSerializers

class ComunidadDetalle(generics.RetrieveUpdateAPIView):
    queryset =  Comunidad.objects.all()
    serializer_class = ComunidadSerializers