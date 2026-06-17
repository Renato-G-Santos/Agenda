from rest_framework import serializers
from .models import *
from django.utils import timezone
from django.contrib.auth.models import User
from .utils import get_horario_diponivel


class AgendamentoSerializer(serializers.ModelSerializer):
    class Meta:
        nome = serializers.ReadOnlyField(source='User.username')
        email = serializers.ReadOnlyField(source='User.email')
        telefone = serializers.ReadOnlyField(source='User.telefone')

        model = Agendamento
        fields = ['id', 'data', 'telefone', 'user', 'estabelecimento', 'evento', 'servico', 'cancelado'] 

    write_only_fields = ['user', 'estabelecimento', 'evento', 'servico']
    
    user = serializers.CharField()

    def validate_user(self, value):
        try:
            user_obj = User.objects.get(id=value)
        except User.DoesNotExist:
            raise serializers.ValidationError("User nao encontrado!")
        return user_obj
    
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
    
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username','password', 'email']   
        User.objects

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




class EstabelecimentoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Estabelecimento
        fields = ['id', 'nome', 'hr_abertura', 'hr_fechamento', 'dc_estabelecimento', 'user', 'endereco']
    
    

class EventoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Evento
        fields = ['id', 'nome', 'dc_evento', 'data_inicio', 'data_fim', 'estabelecimento', 'hr_inicio', 'hr_fim', 'user']

class ServicoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Servico
        fields = ['id', 'nome', 'dc_servico', 'duracao', 'vl_servico', 'estabelecimento', 'evento']

class EnderecoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Endereco
        fields = ['id', 'rua', 'numero', 'bairro', 'cidade', 'estado', 'cep']




class PrestadorSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'agendamentos']

    agendamentos = AgendamentoSerializer(many=True, read_only=True)

