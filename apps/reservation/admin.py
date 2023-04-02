from django.contrib import admin
from django.contrib.admin import ModelAdmin, register
from .models import Reservation
# Register your models here.


@register(Reservation)
class ReservationAdmin(ModelAdmin):
    list_display = (
        'id_reservacion',
        'id_cliente',
        'id_mesa',
        'numero_personas'
    )
    search_fields = ('id_reservacion', 'id_cliente__nombre',)
