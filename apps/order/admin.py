from django.contrib import admin
from django.contrib.admin import ModelAdmin, register
from .models import Order

# Register your models here.


@register(Order)
class OrderAdmin(ModelAdmin):
    list_display = (
        'id_pedido',
        'id_cliente',
        'fecha_hora_pedido',
        'estado_pedido'
    )
    search_fields = ('estado_pedido', 'id_cliente')
