from django.db import models
from django.contrib.auth.models import User

class Curso(models.Model):

    nombre = models.CharField(max_length = 50)
    comision = models.IntegerField()

    def __str__(self):
        return f'{self.nombre} / Comision: {self.comision}'

class Estudiante(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    email = models.EmailField(unique=True)

    def __str__(self):
        return f'{self.nombre.capitalize()} {self.apellido.upper()} --- E-Mail: {self.email}'

class Profesor(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    email = models.EmailField()
    profesion = models.CharField(max_length=100)

    def __str__(self):
        return f'{self.nombre.capitalize()} {self.apellido.upper()} -- {self.profesion.title()}'

class Entregable(models.Model):
    nombre = models.CharField(max_length=100)
    fecha_de_entrega = models.DateField()

    def __str__(self):
        return f'{self.nombre.capitalize()} --> {self.fecha_de_entrega()}'

class Avatar(models.Model):

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    imagen = models.ImageField(upload_to='avatares', null='True', blank='True')