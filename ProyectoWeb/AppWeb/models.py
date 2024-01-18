from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Comida(models.Model):
    nombre = models.CharField(max_length=50)
    descripcion = models.CharField(max_length=100)
    precio = models.IntegerField()
    def __str__(self):
        return self.nombre

class Guarnicion(models.Model):
    nombre = models.CharField(max_length=50)
    descripcion = models.CharField(max_length=100)
    precio = models.IntegerField()
    def __str__(self):
        return self.nombre

class Bebida(models.Model):
    nombre = models.CharField(max_length=50)
    descripcion = models.CharField(max_length=100)
    precio = models.IntegerField()
    def __str__(self):
        return self.nombre

class Postre(models.Model):
    nombre = models.CharField(max_length=50)
    descripcion = models.CharField(max_length=100)
    precio = models.IntegerField()
    def __str__(self):
        return self.nombre

class AvatarImage(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    imagen = models.ImageField(upload_to='avatars', null=True, blank=True)
    