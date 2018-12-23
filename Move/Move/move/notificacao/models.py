from django.db import models

# Create your models here.
class Setor(models.Model):
    nome = models.CharField(max_length=60, null=False)
    esferaPublica = models.CharField(max_length=1, null=False, default='M')