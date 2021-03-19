from django.db import models
from django.utils import timezone
from django.core.validators import MinLengthValidator
from django.contrib.auth.models import User
from django.forms import forms, HiddenInput

# Create your models here.
  
class Cancha(models.Model):
    nombre=models.CharField(max_length=30)
    direccion=models.CharField(max_length=50)
    precio= models.IntegerField()
    

    def __str__(self):
       return self.nombre
        
class Usuario(models.Model):
    nombre=models.CharField(max_length=30)
    email=models.EmailField()
    dni=models.IntegerField()
    
    def __str__(self):
       return self.nombre

class Horario(models.Model):
    hora_inicio=models.TimeField()
    hora_finalizacion=models.TimeField()
    disponible=models.BooleanField()

    
    def __str__(self):
       return str("%s a %s " % (self.hora_inicio, self.hora_finalizacion))

class Reserva(models.Model):
    dia=models.DateField(null=True)
    horario=models.ForeignKey(Horario,on_delete=models.CASCADE, null=False, blank=False)
    usuario=models.ForeignKey(User, on_delete=models.CASCADE, null=False, blank=False)
    #usuario.fields.widget = HiddenInput()
    cancha=models.ForeignKey(Cancha, on_delete=models.CASCADE, null=False, blank=False)   

    def __str__(self):
        return str(self.id)