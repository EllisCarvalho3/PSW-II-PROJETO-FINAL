from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class Usuario(AbstractUser):
    def __str__(self):
        return self.username

class Aluno(models.Model):
    nome = models.CharField(max_length=100)
    idade = models.IntegerField()
    telefone = models.CharField(max_length=20) 
    email = models.EmailField()

    def __str__(self): 
        return self.nome


class Professor(models.Model):
    nome = models.CharField(max_length=100)
    especialidade = models.CharField(max_length=100)
    telefone = models.CharField(max_length=20)

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

    instrumento = models.ForeignKey(
        Instrumento,
        on_delete=models.CASCADE
    )

    professor = models.ForeignKey(
        Professor,
        on_delete=models.CASCADE
    )

    def __str__(self):
        return self.nome


class Matricula(models.Model):
    aluno = models.ForeignKey(
        Aluno,
        on_delete=models.CASCADE
    )

    turma = models.ForeignKey(
        Turma,
        on_delete=models.CASCADE
    )

    data_matricula = models.DateField()

    def __str__(self):
        return f"{self.aluno} - {self.turma}"    