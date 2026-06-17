from django.db import models

# Create your models here.

class Agendamento(models.Model):

    status = [("Pendente", "Pendente"), ("Confirmado", "Confirmado"), ("Cancelado", "Cancelado")]

    user = models.ForeignKey("auth.User", related_name="agendamentos", on_delete=models.CASCADE)
    data = models.DateTimeField()
    telefone = models.CharField(max_length=20)
    status = models.CharField(max_length=20, choices= status, default="Pendente")
    estabelecimento = models.ForeignKey("Estabelecimento", on_delete=models.CASCADE, null=True)
    evento = models.ForeignKey("Evento", on_delete=models.CASCADE, null=True)
    cancelado = models.BooleanField(default=False)
    servico = models.ForeignKey("Servico", related_name="servicos", on_delete=models.CASCADE, null=True)



    def __str__(self):
        return f"{self.user.username, self.user.email} - {self.data}"

class Estabelecimento(models.Model):
    nome = models.CharField(max_length=100, unique=True, null=False)
    hr_abertura = models.TimeField()
    hr_fechamento = models.TimeField()
    dc_estabelecimento = models.TextField()
    user = models.ForeignKey("auth.User", related_name="estabelecimentos", on_delete=models.CASCADE, null=False)
    endereco = models.ForeignKey("Endereco", related_name="estabelecimentos", on_delete=models.CASCADE, null=False)

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
    estabelecimento = models.ForeignKey("Estabelecimento", on_delete=models.CASCADE, null=True)
    evento = models.ForeignKey("Evento", on_delete=models.CASCADE, null=True)

    def __str__(self):
        
        return self.nome

class Evento(models.Model):
    nome = models.CharField(max_length=100)
    dc_evento = models.TextField()
    data_inicio = models.DateTimeField()
    data_fim = models.DateTimeField()
    estabelecimento = models.ForeignKey("Evento", on_delete=models.CASCADE, null=True)
    hr_inicio = models.TimeField()
    hr_fim = models.TimeField()
    user = models.ForeignKey("auth.User", related_name="evento", on_delete=models.CASCADE, null=False)

    def __str__(self):
        return self.nome

