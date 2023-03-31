from django.db import models
from apps.client.models import Client
from apps.table.models import Table

# Create your models here.


class Reservation(models.Model):
    id_reservacion = models.AutoField(primary_key=True)
    id_cliente = models.ForeignKey(Client, on_delete=models.CASCADE)
    id_mesa = models.ForeignKey(Table, on_delete=models.CASCADE)
    fecha_hora_inicio = models.DateTimeField()
    fecha_hora_fin = models.DateTimeField()
    numero_personas = models.IntegerField()
