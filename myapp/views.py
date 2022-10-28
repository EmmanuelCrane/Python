from django.shortcuts import render
from .models import Pelicula

# Create your views here.

def index(reques):
    peliculas = Pelicula.objects.all()
    return render(reques, 'index.html', {"peliculas": peliculas})
