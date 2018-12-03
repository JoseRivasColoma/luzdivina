from django.db import models

# Create your models here.
class Comunidad(models.Model):
    descripcion = models.CharField(max_length=30)
    ubicacion = models.CharField(max_length=30)
    def __str__(self):
        return self.descripcion
    class Meta:
        verbose_name = "Comunidad"
        verbose_name_plural = "Comunidades"

class TipoEvento(models.Model):
    descripcion = models.CharField(max_length=30)
    def __str__(self):
        return self.descripcion
    #subclase que permite nombrar las tablas en el administrador
    class Meta:
        verbose_name = "Tipo de Evento"
        verbose_name_plural = "Tipos de Evento"

class EstadoEvento(models.Model):
    descripcion = models.CharField(max_length=30)
    def __str__(self):
        return self.descripcion
    class Meta:
        verbose_name = "Estado de Evento"
        verbose_name_plural = "Estados de Eventos"

class TipoPersona(models.Model):
    descripcion = models.CharField(max_length=30)
    def __str__(self):
        return self.descripcion
    class Meta:
        verbose_name = "Tipo de Persona"
        verbose_name_plural = "Tipos de Persona"

class Evento(models.Model):
    fecha_evento = models.DateField(auto_now=False, auto_now_add=False)
    hora_evento = models.TimeField(auto_now=False, auto_now_add=False)
    descripcion = models.CharField(max_length=50)
    direccion = models.CharField(max_length=50)
    tipo_evento = models.ForeignKey(TipoEvento, on_delete = models.CASCADE)
    estado_evento = models.ForeignKey(EstadoEvento, on_delete= models.CASCADE)
    def __str__(self):
        return self.descripcion
    class Meta:
        verbose_name = "Evento"
        verbose_name_plural = "Eventos"

class Persona(models.Model):
    nombre = models.CharField(max_length=40)
    apellido = models.CharField(max_length=40)
    edad = models.IntegerField()
    sexo = models.CharField(max_length=20)
    telefono = models.CharField(max_length=15)
    direccion = models.CharField(max_length=50)
    tipo_persona = models.ForeignKey(TipoPersona, on_delete=models.CASCADE)
    tipo_evento = models.ForeignKey(TipoEvento, on_delete=models.CASCADE, null = True)
    comunidad = models.ForeignKey(Comunidad, on_delete = models.CASCADE, null=True)
    def __str__(self):
        return self.nombre + ' ' +self.apellido
    class Meta:
        verbose_name = "Persona"
        verbose_name_plural = "Personas"