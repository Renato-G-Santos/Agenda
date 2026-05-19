from django.shortcuts import render, redirect
from django.shortcuts import get_object_or_404
from .models import agendamento
from .serializes import AgendamentoSerializer
from django.http import JsonResponse 
from rest_framework.decorators import api_view



# Create your views here.

@api_view(['GET', 'PATCH'])
def agendamento_detail(request, id):
    if request.method == 'GET':
        obj = get_object_or_404(agendamento, id=id)
        serializer = AgendamentoSerializer(obj)
        return JsonResponse(serializer.data)
    if request.method in ['PATCH']:
        obj = get_object_or_404(agendamento, id=id)
        serializer = AgendamentoSerializer(data=request.data, partial=True)
        if serializer.is_valid():
            validated_data = serializer.validated_data
            obj.data = validated_data.get('data', obj.data)
            obj.nome = validated_data.get('nome', obj.nome)
            obj.email = validated_data.get('email', obj.email)
            obj.telefone = validated_data.get('telefone', obj.telefone)
            obj.save()
            return JsonResponse(validated_data, status=200)
        return JsonResponse(serializer.errors, status=400)

@api_view(['GET', 'POST'])
def agendamento_list(request):
    if request.method == 'GET':
        qs = agendamento.objects.all()
        serializer = AgendamentoSerializer(qs, many=True)
        return JsonResponse(serializer.data, safe=False)
    if request.method == 'POST':
        serializer = AgendamentoSerializer(data=request.data)
        if serializer.is_valid():
            validated_data = serializer.validated_data
            agendamento.objects.create(
                data = validated_data['data'],
                nome = validated_data['nome'],
                email = validated_data['email'],
                telefone = validated_data['telefone']
            )
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)