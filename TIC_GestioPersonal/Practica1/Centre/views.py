from django.shortcuts import render, redirect
from django.template import loader
from django.http import HttpResponse
from .forms import PersonForm
from . import models

def students(request):
    data =list(models.persona.objects.all())
    alumnos = []
    for person in data:        
        if person.rol == 'estudiant':
            alumnos.append({"id": person.id, "nombre": person.nom, "apellido": person.cognom, "edad": person.edat, "rol": person.rol})
            
    template = loader.get_template('students.html')
    dades = template.render({'alumnos': alumnos})
    return HttpResponse(dades)



data =list(models.persona.objects.all())
profesores = []
for person in data:        
    if person.rol == 'professor':
        profesores.append({"id": person.id, "nombre": person.nom, "apellido": person.cognom, "edad": person.edat, "rol": person.rol})
            

def teachers(request):
    data =list(models.persona.objects.all())
    profesores = []
    for person in data:        
        if person.rol == 'professor':
            profesores.append({"id": person.id, "nombre": person.nom, "apellido": person.cognom, "edad": person.edat, "rol": person.rol})

    template = loader.get_template('teachers.html')
    dades = template.render({'profesores' : profesores})
    return HttpResponse(dades)

def teacher(request, id):
    teacher_obj = None
    for n in profesores:
        if n["id"] == id:
            teacher_obj = n
    return render(request, 'profesor.html', {'prof': teacher_obj})
        
def form(request):
    form = PersonForm(request.POST)
    if form.is_valid():
        form.save()
        return redirect('students')
    
    context ={"form": form}
    return render(request, 'user_form.html', context)


def update_user(request, pk):
    personaData = models.persona.objects.get(id=pk)
    form = PersonForm(instance=personaData)
    
    if request.method == 'POST':
        form = PersonForm(request.POST, instance=personaData)  
        if form.is_valid():
            form.save()
            return redirect('students')
        
    context = {'form': form}
    return render(request, 'update_user.html', context)

def delete_user(request, pk):
    personData = models.persona.objects.get(id=pk)
    
    if request.method == 'POST':
        personData.delete()
        return redirect('students')
    
    context = {'personData' : personData}
    return render(request, 'delete_object.html', context)