from django.shortcuts import render
from rest_framework import viewsets
from .models import Estado,Cidades
from .serializers import  EstadoSerializer,CidadeSerializer

# Create your views here.
class EstadoViewSet(viewsets.ModelViewSet):
    queryset = Estado.objects.all()
    serializer_class = EstadoSerializer


class CidadeViewSet(viewsets.ModelViewSet):
    queryset = Cidades.objects.all()
    serializer_class = CidadeSerializer


    
