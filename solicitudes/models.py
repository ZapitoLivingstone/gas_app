from django.db import models
from datetime import timedelta
from django.utils import timezone

class Solicitud(models.Model):
    ESTADOS = [
        ('P', 'PENDIENTE'),
        ('A', 'ACEPTADA'),
        ('R', 'RECHAZADA'),
        ('E', 'EXPIRADA'),
    ]

    rut = models.CharField(max_length=12)
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    direccion = models.CharField(max_length=255)
    telefono = models.CharField(max_length=15)
    comuna = models.CharField(max_length=100)
    fecha_solicitud = models.DateTimeField(auto_now_add=True) 
    fecha_aceptacion = models.DateTimeField(null=True, blank=True)
    estado = models.CharField(max_length=1, choices=ESTADOS, default='P')

    def es_expirada(self):
        if self.estado == 'A' and self.fecha_aceptacion:
            return timezone.now() > self.fecha_aceptacion + timedelta(days=30)
        return False

    def actualizar_estado(self):
        if self.es_expirada():
            self.estado = 'E'
            self.save()  

    def __str__(self):
        return f"Solicitud de {self.nombre} {self.apellido} (RUT: {self.rut})"
