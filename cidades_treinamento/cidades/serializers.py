from rest_framework import serializers
from .models import Estado, Cidade

class CidadeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cidade
        fields = ['id', 'nome', 'estado']

class EstadoSerializer(serializers.ModelSerializer):
    cidades = CidadeSerializer(many=True, read_only=True)

    class Meta:
        model = Estado
        fields = ['id', 'nome', 'sigla', 'cidades']
