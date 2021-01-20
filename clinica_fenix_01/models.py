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
    edad = models.IntegerField(3)
    rut = models.CharField(max_length=60)
    nacionalidad = models.CharField(max_length=60)
    teléfono = models.IntegerField(11)
    dirección = models.CharField(max_length=60)


