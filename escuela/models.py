from django.db import models


class tabla(models.Model):
    campo1 = models.CharField(max_length=30)
    campo2 = models.CharField(max_length=30)
    campo3 = models.CharField(max_length=30)
    campo4 = models.CharField(max_length=30)
    campo5 = models.CharField(max_length=30)
    campo6 = models.CharField(max_length=30)

class alumno(models.Model):
    name = models.CharField(max_length=30)
    surname = models.CharField(max_length=30)
    

class profesor(models.Model):
    name = models.CharField(max_length=30)
    surname = models.CharField(max_length=30)
   
