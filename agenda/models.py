from django.db import models

# Create your models here.

class agendamento(models.Model):
    data_horario = models.DateTimeField()
    nome = models.CharField(max_length=100)
    email = models.EmailField()
    telefone = models.CharField(max_length=20)
    def __str__(self):
        return f"{self.nome} - {self.data_horario}"