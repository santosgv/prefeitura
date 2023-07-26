from django.db import models

class Usuario(models.Model):

    nome = models.CharField(max_length=30)
    matricula = models.CharField(max_length= 30)
    senha = models.CharField(max_length=64)
    local = models.CharField(max_length=65, default='N/A')
    
    def __str__(self) -> str:
        return self.nome
# Create your models here.