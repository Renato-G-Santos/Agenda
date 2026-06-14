from django.shortcuts import render, redirect
from django.shortcuts import get_object_or_404
from .models import *
from .serializes import *
from django.http import JsonResponse 
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import mixins, generics
from rest_framework import permissions 
from django.contrib.auth.models import User
from .utils import get_horario_diponivel
import datetime






# views your views here.

class isOwnerCreateOnly(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.method == 'POST':
            return True
        username = request.query_params.get('username', None)
        if request.User.username == username:
            return True
        return False


class agendamento_list(generics.ListCreateAPIView):
    serializer_class = AgendamentoSerializer
    permission_classes=[isOwnerCreateOnly]

    def get_queryset(self):
        username = self.request.query_params.get('username', None)
        queryset = Agendamento.objects.filter(prestador__username=username)
        return queryset
    
class isPrestador(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if obj.prestador == request.user:
            return True
        return False

class agendamento_detail(generics.RetrieveUpdateDestroyAPIView
    ):
    permission_classes=[isPrestador]
    queryset = Agendamento.objects.all()
    serializer_class = AgendamentoSerializer

class CreateUser(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class CreateEndereco(generics.CreateAPIView):
    queryset = Endereco.objects.all()
    serializer_class = EnderecoSerializer

class CreateServico(generics.CreateAPIView):
    queryset = Servico.objects.all()
    serializer_class = ServicoSerializer

class CreateEstabelecimento(generics.CreateAPIView):
    queryset = Estabelecimento.objects.all()
    serializer_class = EstabelecimentoSerializer

class CreateEvento(generics.CreateAPIView):
    queryset = Evento.objects.all()
    serializer_class = EventoSerializer


class Prestador_list(generics.ListAPIView):
    permission_classes=[permissions.IsAdminUser]
    serializer_class = PrestadorSerializer
    queryset = User.objects
    queryset = User.objects.all()

@api_view(['GET'])
def get_horarios(request):
    data = request.query_params.get('data', None)
    if not data:
        data = datetime.now().date()
    else:
        data = datetime.datetime.fromisoformat(data).date()
    
    get_horarios = sorted(list(get_horario_diponivel(data)))
    return JsonResponse(get_horarios, safe=False)




@api_view(['GET'])
def health_check(request):
    return JsonResponse({'status': 'ok'}, status=200)