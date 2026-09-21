from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms import ModelForm
from .models import *


class CadastroForm(UserCreationForm):
    email = forms.EmailField(
        required=True,
        label='E-mail',
        widget=forms.EmailInput(attrs={'autocomplete': 'email'}),
    )

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')

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