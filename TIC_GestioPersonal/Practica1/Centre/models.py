from django.db import models

# Create your models here.
class student (models.Model):
    id = models.AutoField(primary_key=True) 
    nom = models.CharField(max_length=100)
    cognom = models.CharField(max_length=100)
    edat= models.IntegerField()
    ESTUDIANT = 'estudiant'
    PROFESSOR = 'professor'
    ROL_CHOICES = [
        (ESTUDIANT, 'Estudiante'),
        (PROFESSOR, 'Profesor'),
    ]
    rol = models.CharField(max_length=50, choices=ROL_CHOICES)
    
class professor ( models.Model):
    id = models.AutoField(primary_key=True) 
    nom = models.CharField(max_length=100)
    cognom = models.CharField(max_length=100)
    edat= models.IntegerField()
    ESTUDIANT = 'estudiant'
    PROFESSOR = 'professor'
    ROL_CHOICES = [
        (ESTUDIANT, 'Estudiante'),
        (PROFESSOR, 'Profesor'),
    ]
    rol = models.CharField(max_length=50, choices=ROL_CHOICES)
    DAW1 = 'DAW1'
    DAW2 = 'DAW2'
    DAM1 = 'DAM1'
    DAM2 = 'DAM2'
    ASIX1 = 'ASIX1'
    ASIX2 = 'ASIX2'
    CURSO_CHOICES = [
        (DAW1, 'DAW1'),
        (DAW2, 'DAW2'),
        (DAM1, 'DAM1'),
        (DAM2, 'DAM2'),
        (ASIX1, 'ASIX1'),
        (ASIX2, 'ASIX2'),
    ]
    curs = models.CharField(max_length=50, choices=CURSO_CHOICES)
    
    
class persona (models.Model):
    id = models.AutoField(primary_key=True) 
    nom = models.CharField(max_length=100)
    cognom = models.CharField(max_length=100)
    edat= models.IntegerField()
    ESTUDIANT = 'estudiant'
    PROFESSOR = 'professor'
    ROL_CHOICES = [
        (ESTUDIANT, 'Estudiante'),
        (PROFESSOR, 'Profesor'),
    ]
    rol = models.CharField(max_length=50, choices=ROL_CHOICES)