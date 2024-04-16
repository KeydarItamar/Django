from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
# Create your views here.

def index(request):
    alumno = {"name": "itamar", "surname": "keydar", "age": 34 }
    template = loader.get_template('index.html')
    dades = template.render({'nombre' : alumno["name"], 'apellido': alumno["surname"], 'edad': alumno["age"]})
    return HttpResponse(dades)

def about(request):
    return HttpResponse("<h2>About</h2>")