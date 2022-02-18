from django.db import models
from datetime import datetime, date

# Create your models here.
class Cliente(models.Model):
    nome = models.CharField(max_length=30, blank=False, null=False)
    sobrenome = models.CharField(max_length=30, blank=False, null=False)
    cpf = models.CharField(max_length=11, blank=False, unique=True)
    email = models.EmailField(max_length=100)
    telefone = models.CharField(max_length=11, blank=False, null=False, unique=True)
    foto = models.ImageField(blank=True, upload_to='fotos/%Y/%m/')
    criado = models.DateField(auto_now_add=True, auto_now=False, blank=True)
    
    def __str__(self):
        return self.nome
