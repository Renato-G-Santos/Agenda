from rest_framework import serializers
from .models import *
from django.utils import timezone


class AgendamentoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Agendamento
        fields = ['id', 'data', 'nome', 'email', 'telefone'] 

    def validate_data(self, value):
        horarios_agendamento = Agendamento.objects.filter(data=value, cancelado=False)
        if value < timezone.now():
            raise serializers.ValidationError("Eventos não podem ser gravado no passado!")
        elif horarios_agendamento.exists():
            raise serializers.ValidationError("Já existe um agendamento para essa data!")
        return value

    def validate(self, attrs):
        telefone = attrs.get("telefone", "")
        email = attrs.get("email",  "")
        if email.endswith(".br") and telefone.startswith("+") and not telefone.startswith("+55"):
            raise serializers.ValidationError("Um email do Brasil deve ter um telefone do Brasil!")
        return attrs

    # def create(self, validated_data):
    #     agendamento = Agendamento.objects.create(
    #         data = validated_data['data'],
    #         nome = validated_data['nome'],
    #         email = validated_data['email'],
    #         telefone = validated_data['telefone']
    #     ) 
    #     return agendamento
    
    # def update(self, instance, validated_data):
            
    #         instance.data = validated_data.get('data', instance.data)
    #         instance.nome = validated_data.get('nome', instance.nome)
    #         instance.email = validated_data.get('email', instance.email)
    #         instance.telefone = validated_data.get('telefone', instance.telefone)
    #         instance.save()
    #         return instance