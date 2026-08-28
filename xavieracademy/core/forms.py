from django.forms import ModelForm
from .models import *

class AlunoForm(ModelForm):
    class Meta:
        model = Aluno
        fields = [
            'username',
            'email',
            'nome',
            'cpf',
            'rg',
            'data_nascimento',
            'sexo',
            'telefone',
            'logradouro',
            'numero',
            'bairro',
            'cidade',
            'estado',
            'cep',
            'status_instituicao',
            'matricula',
        ]

class ProfessorForm(ModelForm):
    class Meta:
        model = Professor
        fields = [
            'username',
            'email',
            'nome',
            'cpf',
            'rg',
            'data_nascimento',
            'sexo',
            'telefone',
            'logradouro',
            'numero',
            'bairro',
            'cidade',
            'estado',
            'cep',
            'status_instituicao',
            'especialidade',
        ]

class InstrumentoForm(ModelForm):
    class Meta:
        model = Instrumento
        fields = [
            'nome',
            'tipo',
            'marca',
        ]

class TurmaForm(ModelForm):
    class Meta:
        model = Turma
        fields = [
            'nome',
            'horario',
            'instrumento',
            'professor',
        ]

class MatriculaForm(ModelForm):
    class Meta:
        model = Matricula
        fields = [
            'aluno',
            'turma',
            'status',
            'data_matricula',
        ]