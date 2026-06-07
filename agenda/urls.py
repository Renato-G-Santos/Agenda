from django.urls import path
from agenda.views import  *
from django.conf.urls import include


urlpatterns = [
    path('agendamentos/', agendamento_list.as_view(), name='agendamento_list'),
    path('agendamentos/<int:pk>/', agendamento_detail.as_view(), name='agendamento_detail'),
    path('prestadores/', Prestador_list.as_view(), name='prestador_list'),
    path('horarios/', get_horarios, name='get_horarios'),
    path('', health_check, name='health_check'),
    path('prestadores/create/', CreateUser.as_view(), name='prestador_create'),
    ]