from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse



def students(request):
    alumnos = [
        {"id": 1, "nombre": "Juan", "apellido": "Pérez", "edad": 20, "rol": "Estudiante", "curso": "1º"},
        {"id": 2, "nombre": "Marta", "apellido": "López", "edad": 22, "rol": "Estudiante", "curso": "2º"},
        {"id": 3, "nombre": "Pedro", "apellido": "González", "edad": 25, "rol": "Estudiante", "curso": "3º"},
        {"id": 4, "nombre": "María", "apellido": "García", "edad": 21, "rol": "Estudiante", "curso": "1º"},
        {"id": 5, "nombre": "Ana", "apellido": "Martínez", "edad": 23, "rol": "Estudiante", "curso": "2º"}]
  
    template = loader.get_template('students.html')
    dades = template.render({'alumnos': alumnos})
    return HttpResponse(dades)


def teachers(request):
    profesores = [
        {"id": 1, "nombre": "Pedro", "apellido": "Martínez", "edad": 35, "rol": "Profesor", "curs": "Informática"},
        {"id": 2, "nombre": "María", "apellido": "López", "edad": 40, "rol": "Profesor", "curs": "Matemáticas"},
        {"id": 3, "nombre": "Juan", "apellido": "González", "edad": 38, "rol": "Profesor", "curs": "Física"},
        {"id": 4, "nombre": "Ana", "apellido": "Sánchez", "edad": 45, "rol": "Profesor", "curs": "Historia"},
        {"id": 5, "nombre": "Laura", "apellido": "Fernández", "edad": 42, "rol": "Profesor", "curs": "Lengua"},
    ]

    template = loader.get_template('teachers.html')
    dades = template.render({'profesores' : profesores})
    return HttpResponse(dades)


profesores = [
    {"id": 1, "nombre": "Pedro", "apellido": "Martínez", "edad": 35, "rol": "Profesor", "curs": "Informática"},
    {"id": 2, "nombre": "María", "apellido": "López", "edad": 40, "rol": "Profesor", "curs": "Matemáticas"},
    {"id": 3, "nombre": "Juan", "apellido": "González", "edad": 38, "rol": "Profesor", "curs": "Física"},
    {"id": 4, "nombre": "Ana", "apellido": "Sánchez", "edad": 45, "rol": "Profesor", "curs": "Historia"},
    {"id": 5, "nombre": "Laura", "apellido": "Fernández", "edad": 42, "rol": "Profesor", "curs": "Lengua"},
]

def teacher(request, id):
    teacher_obj = None
    for n in profesores:
        if n["id"] == id:
            teacher_obj = n
    return render(request, 'profesor.html', {'prof': teacher_obj})
        
# Create your views here.


