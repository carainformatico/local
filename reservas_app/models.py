
from wsgiref.validate import validator
from django.db import models
# Create your models here.

class reserva(models.Model):
    nombre = models.CharField( max_length=30 )
    telefono = models.CharField(max_length=9 , help_text= "ingrese su numero de 9 digitos")
    fecha_de_reserva = models.DateField(help_text= "  aa-mm-dd " )
    hora = models.TimeField()
    cantidad_de_personas = models.IntegerField()
    estado = models.CharField (max_length = 50)
    observacion = models.CharField(max_length = 50)