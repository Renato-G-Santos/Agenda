from django.shortcuts import render, redirect
from django.shortcuts import get_object_or_404
from .models import agendamento
from .serializes import AgendamentoSerializer
from django.http import JsonResponse
from rest_framework.decorators import api_view

# Create your views here.

@api_view(['GET'])
def agendamento_detail(request, id):
    obj = get_object_or_404(agendamento, id=id)
    serializer = AgendamentoSerializer(obj)
    return JsonResponse(serializer.data)

@api_view(['GET'])
def agendamento_list(request):
    qs = agendamento.objects.all()
    serializer = AgendamentoSerializer(qs, many=True)
    return JsonResponse(serializer.data, safe=False)