from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Articulo(models.Model):
    
    nombreArt   = models.CharField(max_length=67)
    modeloArt   = models.CharField(max_length=40)
    # stockArt    = models.IntegerField()
    # precioArt   = models.FloatField()
    # fotoArt     = models.ImageField(upload_to='\static\assets\img', default='NoDisponible.png')
    # def __str__(self):
    #     return f"{self.nombreArt}"

class Comentario(models.Model):
    ideArt      = models.IntegerField()
    fecha       = models.DateField()
    observacion = models.TextField(max_length=10000)


class Usuario(models.Model):
    nombre= models.CharField(max_length=40, null=True)
    apellido= models.CharField(max_length=40, null=True)
    email= models.EmailField(max_length=40, null=True)

    def __str__(self):
        return f"{self.nombre},{self.apellido}"
    

class Contraseña(models.Model):
     claveUsuario= models.CharField(max_length=30)
     clavePass   = models.CharField(max_length=30)


class Admin(models.Model):
    nombre= models.CharField(max_length=40, null=True)
    apellido= models.CharField(max_length=40, null=True)
    email= models.EmailField(max_length=40, null=True)

    def __str__(self):
        return f"{self.nombre},{self.apellido}"


class Avatar(models.Model):
    imagen= models.ImageField(upload_to="avatares")
    user= models.ForeignKey(User, on_delete=models.CASCADE)
    email= models.EmailField(max_length=40, null=True)

    def __str__(self):
        return f"{self.nombre},{self.user} {self.imagen}"

























