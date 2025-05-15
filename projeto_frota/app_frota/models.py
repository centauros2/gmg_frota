from django.db import models
from datetime import datetime
from django.db.models import Q


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


class Empenho(models.Model):
    id_empenho = models.AutoField(primary_key=True)
    numero = models.IntegerField()
    posgra = models.TextField(max_length=100)
    nome = models.TextField(max_length=250)
    placa = models.TextField(max_length=10)
    modelo = models.TextField(max_length=50)
    data_ini = models.DateField(default=datetime.now)

    def __str__(self) -> str:
        return self.placa

    def clean_placa(self):
        nome = self.clean_fields['data_ini']
        return nome.upper()


class Agenda(models.Model):
    id_agenda = models.AutoField(primary_key=True)
    demandante_orgao = models.TextField(max_length=200)
    demandante_pessoa = models.TextField(max_length=250)
    acesso_veiculos = models.BooleanField()
    acesso_pessoas = models.BooleanField()
    acesso_prestadores = models.BooleanField()
    data_agenda = models.DateField(default=datetime.now)
    obs_agenda = models.TextField(max_length=200, null=True, blank=True)
    confirmada_agenda = models.BooleanField(default=False)
    local_agenda = models.TextField(max_length=300)

    class Meta:
        ordering = ('demandante_orgao',)
        verbose_name = 'agenda'
        verbose_name_plural = 'agendas'

    @property
    def agenda_data(self):
        return f'{self.demandante_orgao} {self.data_agenda or ""}'.strip()

    def __str__(self) -> str:
        return self.agenda_data


class Acesso_Pessoa(models.Model):
    id_pessoa = models.ForeignKey(
        Agenda,
        on_delete=models.SET_NULL,
        verbose_name='agenda pessoa',
        null=True,
        blank=True
    )
    nome = models.TextField(max_length=250)
    pessoa_ssp = models.TextField(max_length=100, null=True, blank=True)
    pessoa_cpf = models.TextField(max_length=10, null=True, blank=True)
    confirmada_pessoa = models.BooleanField(default=False)
    data_acesso = models.DateField(default=datetime.now)

    class Meta:
        ordering = ('-pk',)
        verbose_name = 'acesso de pessoa'
        verbose_name_plural = 'acessos de pessoas'

    def __str__(self):
        return f'{self.pk} {self.nome or ""}'.strip()


class Acesso_Veiculo(models.Model):
    id_veiculo = models.ForeignKey(
        Agenda,
        on_delete=models.SET_NULL,
        verbose_name='agenda veiculos',
        null=True,
        blank=True
    )
    placa = models.TextField(max_length=10)
    marca = models.TextField(max_length=50)
    modelo = models.TextField(max_length=50)
    cor = models.TextField(max_length=10)
    confirmada_veiculo = models.BooleanField(default=False)
    data_acesso = models.DateField(default=datetime.now)

    class Meta:
        ordering = ('-pk',)
        verbose_name = 'acesso de veiculo'
        verbose_name_plural = 'acessos de veiculos'

    def __str__(self):
        return f'{self.pk} {self.placa or ""}'.strip()


class Acesso_Prestador(models.Model):
    id_prestador = models.ForeignKey(
        Agenda,
        on_delete=models.SET_NULL,
        verbose_name='agenda prestador',
        null=True,
        blank=True
    )
    nome = models.TextField(max_length=250)
    pessoa_ssp = models.TextField(max_length=100, null=True, blank=True)
    pessoa_cpf = models.TextField(max_length=10, null=True, blank=True)
    confirmada_pessoa = models.BooleanField(default=False)
    data_acesso = models.DateField(default=datetime.now)

    class Meta:
        ordering = ('-pk',)
        verbose_name = 'acesso de prestador'
        verbose_name_plural = 'acessos de prestadores'

    def __str__(self):
        return f'{self.pk} {self.nome or ""}'.strip()
