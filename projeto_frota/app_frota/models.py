from django.db import models
from datetime import datetime


class Usuario(models.Model):
    id_user = models.AutoField(primary_key=True)
    numero = models.IntegerField(unique=True)
    posgra = models.TextField(max_length=100)
    nome = models.TextField(max_length=250)
    cnhcat = models.TextField(max_length=10)
    funcao = models.TextField(max_length=100)
    senha = models.TextField(max_length=12)

    def __str__(self) -> str:
        return str(self.numero)

    def clean_nome(self):
        nome = self.clean_fields['nome']
        if len(nome) > 5:
            raise ValueError("O nome tem que ser completo")
        else:
            return nome.upper()


class Veiculo(models.Model):
    id_car = models.AutoField(primary_key=True)
    placa = models.TextField(max_length=10, unique=True)
    marca = models.TextField(max_length=100)
    modelo = models.TextField(max_length=50)
    cor = models.TextField(max_length=10)
    combustivel = models.TextField(max_length=50)
    data = models.DateField(default=datetime.now)

    def __str__(self) -> str:
        return self.placa

    def clean_placa(self):
        nome = self.clean_fields['placa']
        return nome.upper()
