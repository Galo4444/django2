# appmodelo/models.py
from django.db import models

class Cliente(models.Model):
    id = models.AutoField(primary_key=True)
    nome = models.TextField()
    idade = models.IntegerField()
    email = models.EmailField()
    telefone = models.TextField()
    endereco = models.TextField()

    def __str__(self):
        return self.titulo
