from django.db import models


class tabla(models.Model):
    campo1 = models.CharField(max_length=30)
    campo2 = models.CharField(max_length=30)
    campo3 = models.CharField(max_length=30)
    campo4 = models.CharField(max_length=30)
    campo5 = models.CharField(max_length=30)
    campo6 = models.CharField(max_length=30)
