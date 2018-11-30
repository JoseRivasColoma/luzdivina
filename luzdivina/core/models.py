from django.db import models

# Create your models here.
class Comunidad(models.Model):
    nombre = models.CharField(max_length=50)
    ubicacion = models.CharField(max_length=45)

    def __str__(self):
        return self.nombre