from django.db import models


class Usuarioa(models.Model):

    nome = models.CharField(max_length=30)
    matricula = models.CharField(max_length= 30)
    senha = models.CharField(max_length=64)
    
    def __str__(self) -> str:
        return self.nome

