from django.db import models

# Create your models here.


class Pelicula(models.Model):
    titulo = models.CharField(max_length=50)
    director = models.CharField(max_length=50)
    image = models.CharField(max_length=100)
    descripcion = models.TextField()