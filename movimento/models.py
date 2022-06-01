from datetime import datetime
from django.db import models
from django.contrib.auth.models import User

class ModeloMovimento(models.Model):
    banco_origem = models.CharField(max_length=30, blank=False)
    agencia_origem = models.CharField(max_length=30, blank=False)
    conta_origem = models.CharField(max_length=30, blank=False)
    banco_destino = models.CharField(max_length=30, blank=False)
    agencia_destino = models.CharField(max_length=30, blank=False)
    conta_destino = models.CharField(max_length=30, blank=False)
    valor_da_transacao = models.FloatField(max_length=200, blank=False)
    data_e_hora_da_transacao = models.DateTimeField(blank=False)
    usuario = models.ForeignKey(User, on_delete=models.CASCADE, default=None)
    
class Arquivo(models.Model):
    data_publicacao_banco = models.DateTimeField(default=datetime.now, blank=True)
    data_transacao_banco = models.DateTimeField()
    usuario = models.ForeignKey(User, on_delete=models.CASCADE, default=None)