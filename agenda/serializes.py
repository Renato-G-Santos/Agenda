from rest_framework import serializers
from .models import *


class AgendamentoSerializer(serializers.Serializer):
    data_horario = serializers.DateTimeField()
    nome = serializers.CharField(max_length=100)
    email = serializers.EmailField()
    telefone = serializers.CharField(max_length=20)