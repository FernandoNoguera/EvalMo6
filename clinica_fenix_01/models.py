from django.db import models
from django.core import validators
from django.core.exceptions import ValidationError
import datetime
from django.contrib.auth.models import User 


# Create your models here.
ROLES_CHOISES = [('ADMINISTRADOR', 'administrador'),('CLIENTE', 'cliente')]


class Usuario(models.Model): 
  ## Se refiere a crear o ingresar un paciente nuevo
    usuario = models.OneToOneField(User, on_delete = models.CASCADE)
    rol = models.CharField(max_length=13,choices=ROLES_CHOISES,default="CLIENTE")
    primer_nombre = models.CharField(max_length=25)
    segundo_nombre = models.CharField(max_length=25)
    apellido_paterno = models.CharField(max_length=25)
    apellido_materno = models.CharField(max_length=25)
    edad = models.IntegerField()
    #rut = models.CharField(max_length=15)
    nacionalidad = models.CharField(max_length=60)
    #telefono = models.IntegerField()
    direccion = models.CharField(max_length=50)
    #usuario_id = models.ForeignKey(User,on_delete=models.CASCADE, null =True)

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

