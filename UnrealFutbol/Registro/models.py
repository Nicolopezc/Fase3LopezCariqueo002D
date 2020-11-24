from django.db import models
from django.urls import reverse
import uuid


class Usuario(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    email = models.EmailField(null=True, blank=True)
    fechaN = models.DateField(null=True, blank=True)
    telefono = models.IntegerField(null=True, blank=True)
    password = models.CharField(max_length=6)


    def __str__(self):
        return self.nombre
    
    def get_absolute_url(self):
        return reverse('usuario-detail', args=[str(self.id)])

class Partido(models.Model):
    local = models.CharField(max_length=50)
    visita = models.CharField(max_length=50)
    estadio = models.CharField(max_length=100)
    fecha_partido = models.DateField(null=True, blank=True)
    competicion = models.CharField(max_length=100)

    def __str__(self):
        return self.competicion

    def get_absolute_url(self):
        return reverse('partido-detail', args=[str(self.id)])
   
