from django.db import models

from apps.client.models import Client

# Create your models here.


class Order(models.Model):
    id_pedido = models.AutoField(primary_key=True)
    id_cliente = models.ForeignKey(Client, on_delete=models.CASCADE)
    fecha_hora_pedido = models.DateTimeField(auto_now_add=True)
    ESTADOS = (
        ('EP', 'En preparación'),
        ('L', 'Listo'),
        ('E', 'Entregado'),
        ('C', 'Cancelado'),
    )
    estado_pedido = models.CharField(max_length=2, choices=ESTADOS)

    class Meta:
        verbose_name = "Pedido"
        verbose_name_plural = "Pedidos"
