from django.db import models

# Create your models here.
class Client(models.Model):
    id_cliente = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    correo_electronico = models.EmailField(unique=True)
    numero_de_telefono = models.CharField(max_length=20, unique=True)