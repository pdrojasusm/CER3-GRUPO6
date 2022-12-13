from django.db import models

#superadministrador user = informatica_hospital
#superadministrador contraseña = admin1234

# Create your models here.
class recien_nacido(models.Model):
    id_recien_nacido = models.IntegerField()
    fecha_de_nacimiento = models.DateField()
    hora_de_nacimiento = models.TimeField()
    peso = models.IntegerField()
    fecha_de_ingreso = models.DateField()
    motivo_ingreso = models.CharField(max_length=50)
    rut_madre = models.CharField(max_length=10)
    primera_obs = models.TextField()

class madre_padre(models.Model):
    rut_madre = models.CharField(max_length=10)
    direccion = models.CharField(max_length=50)
    telefono = models.CharField(max_length=15)
    email = models.EmailField()

class seguimiento(models.Model):
    id_seguimiento = models.IntegerField()
    fecha_de_nacimiento = models.DateField()
    unidad = models.CharField(max_length=50)
    cama = models.CharField(max_length=10)
    tiene_orina = models.CharField(max_length=15)
    tiene_deposicion = models.CharField(max_length=15)
    observaciones = models.TextField()
    matrona = models.CharField(max_length=50)
