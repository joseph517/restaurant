from django.db import models

# Create your models here.


class Product(models.Model):
    id_producto = models.AutoField(primary_key=True)
    nombre_producto = models.CharField(max_length=200)
    descripcion_producto = models.TextField()
    precio_producto = models.DecimalField(max_digits=10, decimal_places=2)

    class Meta:
        verbose_name = "Producto"
        verbose_name_plural = "Productos"
