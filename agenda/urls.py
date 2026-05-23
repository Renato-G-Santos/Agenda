from django.urls import path
from agenda.views import  *


urlpatterns = [
    path('agendamentos/', agendamento_list.as_view(), name='agendamento_list'),
    path('agendamentos/<int:pk>/', agendamento_detail.as_view(), name='agendamento_detail'),
    path('prestadores/', Prestador_list.as_view(), name='prestador_list'),
    ]