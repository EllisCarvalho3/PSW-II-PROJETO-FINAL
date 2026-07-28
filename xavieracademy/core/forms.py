from django.forms import ModelForm
from .models import *


class AlunoForm(ModelForm):
    class Meta:
        model = Aluno
        fields = '__all__'


class ProfessorForm(ModelForm): 
    class Meta:
        model = Professor
        fields = '__all__'


class InstrumentoForm(ModelForm):
    class Meta:
        model = Instrumento
        fields = '__all__'


class TurmaForm(ModelForm):
    class Meta:
        model = Turma
        fields = '__all__'


class MatriculaForm(ModelForm):
    class Meta:
        model = Matricula
        fields = '__all__'