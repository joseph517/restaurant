from django.contrib import admin
from django.contrib.admin import ModelAdmin, register
from .models import Client

# Register your models here.


@register(Client)
class ClientAdmin(ModelAdmin):
    list_display = (
        'id',
        'nombre',
        'apellido',
        'correo_electronico',
        'numero_telefono'
    )
    search_fields = ('nombre',)
