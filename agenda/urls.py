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
    path('enderecos/create/', CreateEndereco.as_view(), name='endereco_create'),
    path('servicos/create/', CreateServico.as_view(), name='servico_create'),
    path('estabelecimentos/create/', CreateEstabelecimento.as_view(), name='estabelecimento_create'),
    path('eventos/create/', CreateEvento.as_view(), name='evento_create'),
    ]