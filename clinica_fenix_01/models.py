from django.db import models
from django.core import validators
from django.core.exceptions import ValidationError
import datetime
from django.contrib.auth.models import User 

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
    #usuario_id = models.ForeignKey(User,on_delete=models.CASCADE, null =True)

    class Meta:
        ordering = ['id']



class Profile(models.Model):

    #primer_nombre = models.CharField(max_length=25)
    #segundo_nombre = models.CharField(max_length=25)
    #apellido_paterno = models.CharField(max_length=25)
    #apellido_materno = models.CharField(max_length=25)
    #edad = models.IntegerField()
    usuario = models.OneToOneField(User, on_delete = models.CASCADE)
    descripcion = models.CharField(max_length=70)
    nacionalidad = models.CharField(max_length=100)
    altura = models.DecimalField(max_digits=4, decimal_places=1)
    peso = models.DecimalField(max_digits=4, decimal_places=1)
    direccion = models.CharField(max_length=300)
    codigo_postal = models.CharField(max_length=20)
    archivo_foto = models.CharField(max_length=400, default="sin asignar")
    #rol = models.CharField(max_length=50, default="sin asignar")
    class Meta:
        ordering = ['id']


class Examen(models.Model):   ## Se refiere a crear o ingresar un examen

    plaquetas = models.IntegerField()
    globulos_blancos = models.IntegerField()
    globulos_rojos = models.IntegerField()
    hematocritos = models.IntegerField()
    usuario_id = models.ForeignKey(User,on_delete=models.CASCADE, null =True)

    class Meta:
        ordering = ['id']

