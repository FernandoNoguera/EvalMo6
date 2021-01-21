from django.db import models
from django.core import validators
from django.core.exceptions import ValidationError
import datetime
# Create your models here.


class Usuario(models.Model):   ## Se refiere a crear o ingresar un paciente nuevo

    primer_nombre = models.CharField(
        max_length=60,
        validators=[validators.MinLengthValidator(
                1,
                "Primer nombre no puede tener solo 1  caracter")]
        )
    segundo_nombre = models.CharField(
        max_length=60,
        validators=[validators.MinLengthValidator(
                1,
                "Segundo nombre no puede tener solo 1 caracter")]
        )
    apellido_paterno = models.CharField(
        max_length=60,
        validators=[validators.MinLengthValidator(
                1,
                "Apellido paterno no puede tener solo 1 caracter ")]
        )
    apellido_materno = models.CharField(max_length=60)
    edad = models.IntegerField()
    rut = models.CharField(max_length=60)
    nacionalidad = models.CharField(max_length=60)
    telefono = models.IntegerField()
    direccion = models.CharField(max_length=50)

    class Meta:
        ordering = ['id']


class Examen(models.Model):   ## Se refiere a crear o ingresar un examen

    plaquetas = models.IntegerField()
    globulos_blancos = models.IntegerField()
    globulos_rojos = models.IntegerField()
    hematocritos = models.IntegerField()
    usuario_id = models.ForeignKey(Usuario,on_delete=models.CASCADE, null =True)

    class Meta:
        ordering = ['id']
