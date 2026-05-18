from django.shortcuts import render, redirect
from django.shortcuts import get_object_or_404
from .models import agendamento
from .serializes import AgendamentoSerializer
from django.http import JsonResponse

# Create your views here.


def agendamento_detail(request, id):
    obj = get_object_or_404(agendamento, id=id)
    serializer = AgendamentoSerializer(obj)
    return JsonResponse(serializer.data)

def agendamento_list(request):
    qs = agendamento.objects.all()
    serializer = AgendamentoSerializer(qs, many=True)
    return JsonResponse(serializer.data, safe=False)