from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index' ),
    path('profesores/', views.profes, name='profesores' ),
    path('alumnos/', views.alumns, name='alumnos' ),
]