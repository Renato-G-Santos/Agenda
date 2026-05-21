from django.shortcuts import render, redirect
from django.shortcuts import get_object_or_404
from .models import Agendamento
from .serializes import AgendamentoSerializer
from django.http import JsonResponse 
from rest_framework.decorators import api_view
from rest_framework.response import Response


# Create your views here.

@api_view(['GET', 'PATCH', 'DELETE'])
def agendamento_detail(request, id):
    obj = get_object_or_404(Agendamento, id=id)
    if request.method == 'GET':
        serializer = AgendamentoSerializer(obj)
        return JsonResponse(serializer.data)
    if request.method in ['PATCH']:
        serializer = AgendamentoSerializer(obj, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            
            return JsonResponse(serializer.data, status=200)
        return JsonResponse(serializer.errors, status=400)
    if request.method == 'DELETE':
        obj.cancelado = True
        obj.save()
        return Response(status=204)
    
@api_view(['GET', 'POST',])
def agendamento_list(request):
    if request.method == 'GET':
        qs = Agendamento.objects.filter(cancelado=False)
        serializer = AgendamentoSerializer(qs, many=True)
        return JsonResponse(serializer.data, safe=False)
    if request.method == 'POST':
        serializer = AgendamentoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)