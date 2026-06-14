from django.db import models

# Create your models here.

class Agendamento(models.Model):

    status = [("Pendente", "Pendente"), ("Confirmado", "Confirmado"), ("Cancelado", "Cancelado")]

    user_id = models.ForeignKey("auth.User", related_name="agendamentos", on_delete=models.CASCADE)
    data = models.DateTimeField()
    telefone = models.CharField(max_length=20)
    status = models.CharField(max_length=20, choices= status, default="Pendente")
    estabelecimento_id = models.ForeignKey("Estabelecimento", on_delete=models.CASCADE, null=True)
    evento_id = models.ForeignKey("Evento", on_delete=models.CASCADE, null=True)
    servico_id = models.ForeignKey("Servico", on_delete=models.CASCADE, null=True)
    cancelado = models.BooleanField(default=False)
    


    def __str__(self):
        return f"{self.user.username, self.user.email} - {self.data}"

class Estabelecimento(models.Model):
    nome = models.CharField(max_length=100, unique=True, null=False)
    hr_abertura = models.TimeField()
    hr_fechamento = models.TimeField()
    dc_estabelecimento = models.TextField()
    user_id = models.ForeignKey("auth.User", related_name="estabelecimento", on_delete=models.CASCADE, null=False)
    endereco_id = models.ForeignKey("Endereco", on_delete=models.CASCADE, null=False)
    
    def __str__(self):
        return self.nome
    
class Endereco(models.Model):
    rua = models.CharField(max_length=200)
    numero = models.CharField(max_length=10)
    bairro = models.CharField(max_length=100)
    cidade = models.CharField(max_length=100)
    estado = models.CharField(max_length=100)
    cep = models.CharField(max_length=20)

    def __str__(self):
        return f"{self.rua}, {self.numero} - {self.bairro}, {self.cidade}/{self.estado}"

class Servico(models.Model):
    nome = models.CharField(max_length=100)
    dc_servico = models.TextField()
    duracao = models.DurationField()
    vl_servico = models.DecimalField(max_digits=10, decimal_places=2)
    estabelecimento_id = models.ForeignKey("Estabelecimento", on_delete=models.CASCADE, null=False)
    evento_id = models.ForeignKey("Evento", on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.nome

class Evento(models.Model):
    nome = models.CharField(max_length=100)
    dc_evento = models.TextField()
    data_inicio = models.DateTimeField()
    data_fim = models.DateTimeField()
    estabelecimento_id = models.ForeignKey("Evento", on_delete=models.CASCADE, null=True)
    hr_inicio = models.TimeField()
    hr_fim = models.TimeField()
    user_id = models.ForeignKey("auth.User", related_name="evento", on_delete=models.CASCADE, null=False)

    def __str__(self):
        return self.nome

