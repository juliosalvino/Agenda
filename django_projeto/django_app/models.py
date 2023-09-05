from django.db import models

# Create your models here.

#Criando nossas tabelas:

class eventos(models.Model):
    titulo = models.CharField(max_length = 255)
    descricao = models.TextField(blank= True, null= True)
    data_evento = models.DateTimeField()
    data_criacao = models.DateTimeField(auto_now=True)