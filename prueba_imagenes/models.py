# models.py
from django.db import models

class Producto(models.Model):
    nombre = models.CharField(max_length=100)
    imagen = models.CharField(max_length=255)  # Guarda la ruta de la imagen estática

    def __str__(self):
        return self.nombre