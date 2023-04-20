from django.contrib import admin
from django.contrib.admin import ModelAdmin, register
from .models import Product, Type

# Register your models here.


@register(Product)
class ProductAdmin(ModelAdmin):
    list_display = (
        'id_producto',
        'nombre_producto',
        'descripcion_producto',
        'precio_producto',
    )
    search_fields = ('nombre_producto',)

@register(Type)
class TypeAdmin(ModelAdmin):
    list_display = (
        'nombre',
    )
    search_fields = ('nombre',)
