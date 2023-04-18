from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from django.utils import timezone
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin



# Create your models here.

class CustomUserManager(BaseUserManager):
    def create_user(self, correo_electronico, password=None, **extra_fields):
        if not correo_electronico:
            raise ValueError("El campo correo electrónico es obligatorio.")
        correo_electronico = self.normalize_email(correo_electronico)
        user = self.model(correo_electronico=correo_electronico, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, correo_electronico, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)

        if extra_fields.get("is_staff") is not True:
            raise ValueError("Superuser debe tener is_staff=True.")
        if extra_fields.get("is_superuser") is not True:
            raise ValueError("Superuser debe tener is_superuser=True.")

        return self.create_user(correo_electronico, password, **extra_fields)



class Client(AbstractBaseUser, PermissionsMixin):

    id = models.AutoField(
        primary_key=True,
        null=False,
        blank=False,
        default=None,
        unique=True
    )

    nombre = models.CharField(
        max_length=255, 
        null=False,
        blank=False,
        default=None,
    )

    apellido = models.CharField(
        max_length=100,
        null=False,
        blank=False,    
    )

    correo_electronico = models.EmailField(unique=True)

    numero_telefono = PhoneNumberField(
        verbose_name="Celular",
        null=False,
        blank=False,
        unique=True
    )
    is_active = models.BooleanField(default=True)

    is_staff = models.BooleanField(default=False)

    password = models.CharField(
        max_length=128, 
        null=False, 
        blank=False,
        default=None,
    )


    class Meta:
        verbose_name = 'Cliente'
        verbose_name_plural = 'Clientes'

    

    objects = CustomUserManager()

    USERNAME_FIELD = "correo_electronico"
    REQUIRED_FIELDS = ["nombre", "apellido", "numero_telefono"]  

    def __str__(self):
        return self.correo_electronico
