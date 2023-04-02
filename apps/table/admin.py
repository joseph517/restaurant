from django.contrib import admin
from django.contrib.admin import ModelAdmin, register
from .models import Table, TableSchedule

# Register your models here.


@register(Table)
class TableAdmin(ModelAdmin):
    list_display = (
        'id_mesa',
        'numero_mesa',
        'capacidad_mesa',
    )
    search_fields = ('numero_mesa',)


@register(TableSchedule)
class TableScheduleAdmin(ModelAdmin):
    list_display = (
        'id_horario_mesa',
        'id_mesa',
        'dia_semana',
        'hora_apertura',
        'hora_cierre'
    )
    search_fields = ('dia_semana', 'id_mesa__numero_mesa',)
