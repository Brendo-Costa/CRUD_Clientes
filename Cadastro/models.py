from django.db import models

# Create your models here.
class Cliente(models.Model):
    nome = models.CharField(max_length = 30, blank = False, null = False)
    sobrenome = models.CharField(max_length = 30, blank = False, null = False)
    cpf = models.IntegerField(blank=False)
    email = models.EmailField(max_length = 100)
    telefone = models.IntegerField(blank=False)

    
    def __str__(self):
        return self.nome

