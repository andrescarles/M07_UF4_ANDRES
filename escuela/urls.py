from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index' ),
    path('profesores/', views.profes, name='profesores' ),
    path('profesores/<str:nombre>', views.profes2, name='profesores' ),
    path('alumnos/', views.alumns, name='alumnos' ),
    path('alumnos/<str:nombre>', views.alumns2, name='alumnos' ),
    path('formulario_profe/', views.formulario_profe, name='formulario_profe' ),
    path('formulario_alumno/', views.formulario_alumno, name='formulario_alumno' ),
    path('update-profe/<str:pk>/', views.update_profe, name='update_profe' ),
    path('update-alumno/<str:pk>/', views.update_alumno, name='update_alumno' ),
]


