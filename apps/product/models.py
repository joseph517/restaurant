from django.utils import timezone
from django.db import models

# Create your models here.

class Type(models.Model):
    nombre = models.CharField(
        max_length=255,
        null=False,
        blank=False,
        default=None,
        unique=True
    )

    class Meta:
        verbose_name = "tipo"
        verbose_name_plural = "tipos"


class Product(models.Model):
    id_producto = models.AutoField(primary_key=True)
    nombre_producto = models.CharField(
        max_length=200,
        null=False,
        blank=False,
        default=None,
        unique=True
    )

    descripcion_producto = models.TextField(
        null=False,
        blank=False,
        default=None
    )

    precio_producto = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        null=False,
        blank=False,
        default=None
    )

    tipo_producto = models.ForeignKey(Type, on_delete=models.CASCADE, null=False, blank=True)

    created_at = models.DateTimeField(
        verbose_name="Fecha de Creación",
        default=timezone.now,
    )
    updated_at = models.DateTimeField(default=timezone.now)


    class Meta:
        verbose_name = "Producto"
        verbose_name_plural = "Productos"
