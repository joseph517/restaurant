from django.db import models
from django.core.validators import MinValueValidator

# Create your models here.
class Table(models.Model):
    id_mesa = models.AutoField(primary_key=True)
    numero_mesa = models.IntegerField(unique=True)
    capacidad_mesa = models.IntegerField(validators=[MinValueValidator(1)])

class TableSchedule(models.Model):
    id_horario_mesa = models.AutoField(primary_key=True)
    id_mesa = models.ForeignKey(Table, on_delete=models.CASCADE)
    DIA_SEMANA = (
        ('L', 'Lunes'),
        ('M', 'Martes'),
        ('X', 'Miércoles'),
        ('J', 'Jueves'),
        ('V', 'Viernes'),
        ('S', 'Sábado'),
        ('D', 'Domingo'),
    )
    dia_semana = models.CharField(max_length=1, choices=DIA_SEMANA)
    hora_apertura = models.TimeField()
    hora_cierre = models.TimeField()
