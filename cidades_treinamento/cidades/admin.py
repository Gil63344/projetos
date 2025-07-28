from django.contrib import admin
from .models import Estado, Cidades

@admin.register(Estado)
class EstadoAdmin(admin.ModelAdmin):
    list_display = ('id', 'nome', 'uf','total_cidades')
    search_fields = ('nome', 'uf')
    list_filter = ('uf',)

    def total_cidades(self, obj):
        return obj.cidades.count()
    total_cidades.short_description = 'Cidades'

@admin.register(Cidades)
class CidadeAdmin(admin.ModelAdmin):
    list_display = ['id', 'nome','estado']
    search_fields = ['nome', 'estado__nome']
    list_filter = ['estado__uf']

   
