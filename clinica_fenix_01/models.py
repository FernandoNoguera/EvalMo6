from django.db import models

# Create your models here.


class Usuario(models.Model):

    primer_nombre = models.CharField(max_length=60)
    segundo_nombre = models.CharField(max_length=60)
    apellido_paterno = models.CharField(max_length=60)
    apellido_materno = models.CharField(max_length=60)
    edad = models.IntegerField(3)
    rut = models.CharField(max_length=60)
    nacionalidad = models.CharField(max_length=60)
    teléfono = models.IntegerField(11)
    dirección = models.CharField(max_length=60)

