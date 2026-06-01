from rest_framework import serializers
from .models import *
from django.utils import timezone
from django.contrib.auth.models import User
from .utils import get_horario_diponivel


class AgendamentoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Agendamento
        fields = ['id', 'data', 'nome', 'email', 'telefone', 'prestador'] 

    prestador = serializers.CharField()

    def validate_prestador(self, value):
        try:
            prestador_obj = User.objects.get(username=value)
        except User.DoesNotExist:
            raise serializers.ValidationError("Username nao encontrado!")
        return prestador_obj

    def validate_data(self, value):
        horarios_agendamento = Agendamento.objects.filter(data=value, cancelado=False)
        if value < timezone.now():
            raise serializers.ValidationError("Eventos não podem ser gravado no passado!")
        elif horarios_agendamento.exists():
            raise serializers.ValidationError("Já existe um agendamento para essa data!")
        if value not in get_horario_diponivel(value.date()):
            raise serializers.ValidationError("esse horario não está disponivel!")
        return value

    def validate(self, attrs):
        telefone = attrs.get("telefone", "")
        email = attrs.get("email",  "")
        if email.endswith(".br") and telefone.startswith("+") and not telefone.startswith("+55"):
            raise serializers.ValidationError("Um email do Brasil deve ter um telefone do Brasil!")
        return attrs
    
class PrestadorSerializer(serializers.ModelSerializer):

    password = serializers.CharField(write_only=True)
    class Meta:
        model = User
        fields = ['username', 'email', 'password']   
    def create(self, validated_data):
        
        password = validated_data.pop('password')
        
        user = User.objects.create_superuser(**validated_data)
        user.set_password(password)
        user.save()
        
        return user

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






class PrestadorSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'agendamentos']

    agendamentos = AgendamentoSerializer(many=True, read_only=True)

