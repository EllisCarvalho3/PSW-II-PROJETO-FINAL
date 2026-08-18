<<<<<<< HEAD
from django.db import models
from django.contrib.auth.models import User
class Usuario(User):
    def __str__(self):
        return self.username


class Pessoa(User):
    usuario = models.OneToOneField(
        Usuario,
        on_delete=models.CASCADE,
        null=True,
        blank=True
    )

=======
from django.conf import settings
from django.contrib.auth.models import AbstractUser
from django.db import models

class Usuario(AbstractUser):
    def __str__(self):
        return self.username

class Pessoa(Usuario):
    usuario = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True, blank=True)
>>>>>>> 9692df17f3a99b9cd51df52866512fb7919e757c
    nome = models.CharField(max_length=100)
    cpf = models.CharField(max_length=14, null=True, blank=True)
    rg = models.CharField(max_length=20)
    data_nascimento = models.DateField()
    sexo = models.CharField(max_length=20)
    telefone = models.CharField(max_length=20)
    logradouro = models.CharField(max_length=150)
    numero = models.IntegerField()
    bairro = models.CharField(max_length=100)
    cidade = models.CharField(max_length=100)
    estado = models.CharField(max_length=2)
    cep = models.CharField(max_length=9)

    STATUS_CHOICES = [
        ('ATIVO', 'Ativo'),
        ('INATIVO', 'Inativo'),
    ]

    status_instituicao = models.CharField(max_length=10, choices=STATUS_CHOICES, default='ATIVO')

    def __str__(self):
        return self.nome


class Aluno(Pessoa):
    matricula = models.CharField(max_length=20)

    def __str__(self):
        return self.nome


class Professor(Pessoa):
    especialidade = models.CharField(max_length=100)

    def __str__(self):
        return self.nome


class Instrumento(models.Model):
    nome = models.CharField(max_length=100)
    tipo = models.CharField(max_length=100)
    marca = models.CharField(max_length=100)

    def __str__(self):
        return self.nome


class Turma(models.Model):
    nome = models.CharField(max_length=100)
    horario = models.CharField(max_length=50)
    instrumento = models.ForeignKey(Instrumento, on_delete=models.CASCADE)
    professor = models.ForeignKey(Professor, on_delete=models.CASCADE)

    def __str__(self):
        return self.nome


class Matricula(models.Model):

    STATUS_CHOICES = [
        ('ATIVA', 'Ativa'),
        ('TRANCADA', 'Trancada'),
        ('CANCELADA', 'Cancelada'),
    ]

    aluno = models.ForeignKey(Aluno, on_delete=models.CASCADE, related_name='matriculas')
    turma = models.ForeignKey(Turma, on_delete=models.CASCADE, related_name='matriculas')
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='ATIVA')
    data_matricula = models.DateField()

    def __str__(self):
        return f'{self.aluno} - {self.turma}'