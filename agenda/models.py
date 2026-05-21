from django.db import models

# Create your models here.

class Agendamento(models.Model):
    data = models.DateTimeField()
    nome = models.CharField(max_length=100)
    email = models.EmailField()
    telefone = models.CharField(max_length=20)
    cancelado = models.BooleanField(default=False)
    def __str__(self):
        return f"{self.nome} - {self.data}"