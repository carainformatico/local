from django.db import models

# Create your models here.

class reserva(models.Model):
    nombre = models.CharField(max_length=50)
    telefono = models.CharField(max_length=9 , help_text= "ingrese su numero de 9 digitos")
    fecha_de_reserva = models.DateField(help_text= "  aa/mm/dd " )
    hora = models.TimeField()
    cantidad_de_personas = models.IntegerField(max_length=15)
    estado = models.CharField (max_length = 50)
    observacion = models.CharField(max_length = 50)