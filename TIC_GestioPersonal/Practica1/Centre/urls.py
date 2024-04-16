from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('centre/students/', views.students, name='students'),
    path('centre/teachers/', views.teachers, name='teachers'),
    path('centre/teacher/<int:id>/', views.teacher, name='teacher')
]