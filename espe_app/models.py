from django.db import models
import datetime

# Create your models here.

class Usuario(models.Model):
    username=models.CharField(max_length=220)
    password=models.CharField(max_length=220)

    def __unicode__(self):
        return self.username

class Alumno(models.Model):
    id = models.AutoField(primary_key=True)
    ci = models.CharField(max_length=220)
    nombre = models.CharField(max_length=220)
    apellido = models.CharField(max_length=220)
    anio = models.CharField(max_length=100)
    termino = models.CharField(max_length=100)
    cal1 = models.FloatField()
    cal2 = models.FloatField()
    cal3 = models.FloatField()
    estado = models.CharField(max_length=100)

    def __unicode__(self):
        return self.nombre + " " + self.apellido

class Noticia(models.Model):
    id = models.AutoField(primary_key=True)
    titulo = models.CharField(max_length=220, default="")
    descripcion = models.TextField()
    fecha_publicacion = models.DateField(default=datetime.datetime.now())
    ruta_imagen = models.CharField(max_length=1000, default="", null=True)
    esta_publicado = models.BooleanField(default=False)
    activo = models.BooleanField(default=True)
    borrado = models.BooleanField(default=False)

    def __unicode__(self):
        return self.titulo