from django.conf import settings
from django.db import models
from django.utils import timezone

class Animal(models.Model):
    Cuidador = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    Nombre = models.CharField(max_length=200)
    Tipo = models.TextField()
    
class Protectora(models.Model):
    Nombre = models.CharField(max_length=200)
    Descripcion = models.TextField()
    Fecha_creacion = models.DateTimeField(default=timezone.now)

class Colaborador(models.Model):
    Nombre = models.CharField(max_length=200)
    Cargo = models.CharField(max_length=200)
    Fecha_entrada_protectora = models.DateTimeField(default=timezone.now)