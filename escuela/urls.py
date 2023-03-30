from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index' ),
    path('profesores/', views.profes, name='profesores' ),
    path('profesores/<str:nombre>', views.profes2, name='profesores' ),
    path('alumnos/', views.alumns, name='alumnos' ),
    path('alumnos/<str:nombre>', views.alumns2, name='alumnos' ),
    
]