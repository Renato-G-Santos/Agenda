from rest_framework.test import APITestCase
import json
from .models import *

# Create your tests here.

# class test_listagem_vazia(APITestCase):
    # def test_listagem_vazia(self):
    #     response = self.client.get("/api/agendamentos/")
    #     data = json.loads(response.content)
    #     self.assertEqual(data, [])

# class test_criacao_agendamento(APITestCase):
#     def test_criacao_agendamento(self):
#         pass
#         data={
#         "data": "2026-09-18T19:13:47Z",
#         "nome": "hotal",
#         "email": "hotel@gmail.com",
#         "telefone": "656565342353"
#         }
#         agendamentoSerializer = {
#         "id": 1,
#         "data": "2026-09-18T19:13:47Z",
#         "nome": "hotal",
#         "email": "hotel@gmail.com",
#         "telefone": "656565342353"
#         }
#         response = self.client.post("/api/agendamentos/", data=data)
#         resp = json.loads(response.content)
#         agendamento_obj = Agendamento.objects.get(id=1)
#         self.assertEqual(agendamento_obj.nome, data['nome'])
#         self.assertEqual(response.status_code, 201)
#         self.assertDictEqual(resp, agendamentoSerializer)

# class test_bad_resquest_inexistente_404(APITestCase):
#     def test_bad_resquest_inexistente_404(self):
#         response = self.client.get(f"/api/agendamentos/1/")
#         self.assertEqual(response.status_code, 404)

class test_get_horario(APITestCase):
    def test_retorna_lista_vazia()