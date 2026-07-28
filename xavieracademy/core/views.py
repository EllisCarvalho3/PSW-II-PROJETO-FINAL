from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import *
from .forms import *

# Create your views here.
def index(request):
    return render(request, 'index.html')

# esse crud é para aluno
@login_required
def list_aluno(request):
    alunos = Aluno.objects.all()
    return render(request, 'aluno/list.html', {'alunos': alunos})

@login_required
def create_aluno(request):
    if request.method == 'POST':
        form = AlunoForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('/aluno/')

    else:
        form = AlunoForm()

    return render(request, 'form.html', {'form': form})

def update_aluno(request, id):
    aluno = Aluno.objects.get(id=id)

    if request.method == 'POST':
        form = AlunoForm(request.POST, instance=aluno)

        if form.is_valid():
            form.save()
            return redirect('/aluno/')

    else:
        form = AlunoForm(instance=aluno)

    return render(request, 'form.html', {'form': form})


def detail_aluno(request, id):
    aluno = Aluno.objects.get(id=id)
    return render(request, 'aluno/detail.html', {'aluno': aluno})

def delete_aluno(request, id):
    aluno = Aluno.objects.get(id=id)
    aluno.delete()

    return redirect('/aluno/')
# esse crud é para aluno
# 





# esse crud é para instrumento
def list_instrumento(request):
    instrumentos = Instrumento.objects.all()
    return render(request, 'instrumento/list.html', {'instrumentos': instrumentos})

def create_instrumento(request):
    if request.method == 'POST':
        form = InstrumentoForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('/instrumento/')

    else:
        form = InstrumentoForm()

    return render(request, 'form.html', {'form': form})

def update_instrumento(request, id):
    instrumento = Instrumento.objects.get(id=id)

    if request.method == 'POST':
        form = InstrumentoForm(request.POST, instance=instrumento)

        if form.is_valid():
            form.save()
            return redirect('/instrumento/')

    else:
        form = InstrumentoForm(instance=instrumento)

    return render(request, 'form.html', {'form': form})


def detail_instrumento(request, id):
    instrumento = Instrumento.objects.get(id=id)
    return render(request, 'instrumento/detail.html', {'instrumento': instrumento})

def delete_instrumento(request, id):
    instrumento = Instrumento.objects.get(id=id)
    instrumento.delete()

    return redirect('/instrumento/')

# esse crud é para instrumento



# esse crud é para matricula
def list_matricula(request):
    matriculas = Matricula.objects.all()
    return render(request, 'matricula/list.html', {'matriculas': matriculas})

def create_matricula(request):
    if request.method == 'POST':
        form = MatriculaForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('/matricula/')
 
    else:
        form = MatriculaForm()

    return render(request, 'form.html', {'form': form})

def update_matricula(request, id):
    matricula = Matricula.objects.get(id=id)

    if request.method == 'POST':
        form = MatriculaForm(request.POST, instance=matricula)

        if form.is_valid():
            form.save()
            return redirect('/matricula/')

    else:
        form = MatriculaForm(instance=matricula)

    return render(request, 'form.html', {'form': form})


def detail_matricula(request, id):
    matricula = Matricula.objects.get(id=id)
    return render(request, 'matricula/detail.html', {'matricula': matricula})

def delete_matricula(request, id):
    matricula = Matricula.objects.get(id=id)
    matricula.delete()

    return redirect('/matricula/')
# esse crud é para matricula




# esse crud é para professor
def list_professor(request):
    professores = Professor.objects.all()
    return render(request, 'professor/list.html', {'professores': professores})

def create_professor(request):
    if request.method == 'POST':
        form = ProfessorForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('/professor/')

    else:
        form = ProfessorForm()

    return render(request, 'form.html', {'form': form})

def update_professor(request, id):
    professor = Professor.objects.get(id=id)

    if request.method == 'POST':
        form = ProfessorForm(request.POST, instance=professor)

        if form.is_valid():
            form.save()
            return redirect('/professor/')

    else:
        form = ProfessorForm(instance=professor)

    return render(request, 'form.html', {'form': form})


def detail_professor(request, id):
    professor = Professor.objects.get(id=id)
    return render(request, 'professor/detail.html', {'professor': professor})

def delete_professor(request, id):
    professor = Professor.objects.get(id=id)
    professor.delete()

    return redirect('/professor/')

# esse crud é para professor





# esse crud é para turma
def list_turma(request):
    turmas = Turma.objects.all()
    return render(request, 'turma/list.html', {'turmas': turmas})

def create_turma(request):
    if request.method == 'POST':
        form = TurmaForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('/turma/')

    else:
        form = TurmaForm()

    return render(request, 'form.html', {'form': form})

def update_turma(request, id):
    turma = Turma.objects.get(id=id)

    if request.method == 'POST':
        form = TurmaForm(request.POST, instance=turma)

        if form.is_valid():
            form.save()
            return redirect('/turma/')

    else:
        form = TurmaForm(instance=turma)

    return render(request, 'form.html', {'form': form})


def detail_turma(request, id):
    turma = Turma.objects.get(id=id)
    return render(request, 'turma/detail.html', {'turma': turma})

def delete_turma(request, id):
    turma = Turma.objects.get(id=id)
    turma.delete()

    return redirect('/turma/')
# esse crud é para turma