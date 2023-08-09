from django.db import models
from login.models import Usuario

class Chamado(models.Model):
    tipo = models.CharField(max_length=15)
    localpro = models.CharField(max_length=30)
    demanda = models.CharField(max_length=300)
    usuario = models.ForeignKey(Usuario, on_delete=models.DO_NOTHING)
    def _str_(self) -> str:
        return self.tipo
# Create your models here.