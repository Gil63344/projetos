from django.contrib import admin
from clientes.models import Cliente


# Register your models here.


class ClienteAdmin(admin.ModelAdmin):
    list_display = ['nome','email']
    list_filter = ['nome']
    search_fields = ['nome']
    
admin.site.register(Cliente,ClienteAdmin)