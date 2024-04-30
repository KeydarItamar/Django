from django.contrib import admin
from django.urls import path
from . import views


urlpatterns = [
    path('centre/students/', views.students, name='students'),
    path('centre/teachers/', views.teachers, name='teachers'),
    path('centre/teacher/<int:id>/', views.teacher, name='teacher'),
    path('centre/crearUsuari', views.form, name='form'),
    path('centre/editarUsuari/<str:pk>/', views.update_user, name='update-user'),
    path('centre/deleteUsuari/<str:pk>/', views.delete_user, name='delete-user')
]