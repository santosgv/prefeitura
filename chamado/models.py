from django.db import models
from login.models import Usuario
from logadm.models import Usuarioa
from datetime import datetime

class Chamado(models.Model):
    tipo = models.CharField(max_length=15)
    localpro = models.CharField(max_length=30)
    demanda = models.CharField(max_length=300)
    usuario = models.ForeignKey(Usuario, on_delete=models.DO_NOTHING)
    tecnico = models.ForeignKey(Usuarioa, on_delete=models.DO_NOTHING, default=1)
    data_cadastro = models.DateTimeField(default= datetime.today)
    data_finalizado = models.DateField(null=True, blank=True)
    status = models.CharField(max_length=40, default='Pendente')
    unidade = models.CharField(max_length=65, default='N/A')
    solucao = models.CharField(max_length=399, default='N/A')
    def _str_(self) -> str:
        return self.tipo
# Create your models here.