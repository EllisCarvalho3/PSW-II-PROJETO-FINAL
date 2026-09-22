from functools import wraps
from django.contrib.auth import login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.views import redirect_to_login 
from django.shortcuts import render, redirect
from .forms import CadastroForm
from .models import *
from .forms import *


def admin_required(view_func):
    @wraps(view_func)
    def wrapped_view(request, *args, **kwargs):
        if not request.user.is_authenticated:
            return redirect_to_login(request.get_full_path(), '/accounts/login/')
        if not request.user.is_superuser:
            return render(request, 'registration/unauthorized.html', status=403)
        return view_func(request, *args, **kwargs)

    return wrapped_view


# Create your views here.
def index(request):
    return render(request, 'index.html')


def about(request):
    return render(request, 'about.html')


def videos(request):
    return render(request, 'videos.html')


def cadastro(request):
    if request.method == 'POST':
        form = CadastroForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = CadastroForm()

    return render(request, 'registration/signup.html', {'form': form})


def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            if not user.is_superuser:
                logout(request)
                return render(request, 'registration/login.html', {
                    'form': form,
                    'authorization_error': True,
                })

            login(request, user)
            return redirect(request.POST.get('next') or 'index')
    else:
        form = AuthenticationForm(request)

    return render(request, 'registration/login.html', {'form': form})

# esse crud é para aluno
@admin_required
def list_aluno(request):
    alunos = Aluno.objects.all()
    return render(request, 'aluno/list.html', {'alunos': alunos})


@admin_required
def create_aluno(request):
    if request.method == 'POST':
        form = AlunoForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('/aluno/')
    else:
        form = AlunoForm()

    return render(request, 'form.html', {'form': form})


@admin_required
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


@admin_required
def detail_aluno(request, id):
    aluno = Aluno.objects.get(id=id)

    return render(request, 'aluno/detail.html', {'aluno': aluno})


@admin_required
def delete_aluno(request, id):
    aluno = Aluno.objects.get(id=id)

    aluno.delete()

    return redirect('/aluno/')
# esse crud é para aluno
# 





# esse crud é para instrumento
@admin_required
def list_instrumento(request):
    instrumentos = Instrumento.objects.all()
    return render(request, 'instrumento/list.html', {'instrumentos': instrumentos})

@admin_required
def create_instrumento(request):
    if request.method == 'POST':
        form = InstrumentoForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('/instrumento/')

    else:
        form = InstrumentoForm()

    return render(request, 'form.html', {'form': form})

@admin_required
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


@admin_required
def detail_instrumento(request, id):
    instrumento = Instrumento.objects.get(id=id)
    return render(request, 'instrumento/detail.html', {'instrumento': instrumento})

@admin_required
def delete_instrumento(request, id):
    instrumento = Instrumento.objects.get(id=id)
    instrumento.delete()

    return redirect('/instrumento/')

# esse crud é para instrumento



# esse crud é para matricula
@admin_required
def list_matricula(request):
    matriculas = Matricula.objects.all()
    return render(request, 'matricula/list.html', {'matriculas': matriculas})

@admin_required
def create_matricula(request):
    if request.method == 'POST':
        form = MatriculaForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('/matricula/')
 
    else:
        form = MatriculaForm()

    return render(request, 'form.html', {'form': form})

@admin_required
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


@admin_required
def detail_matricula(request, id):
    matricula = Matricula.objects.get(id=id)
    return render(request, 'matricula/detail.html', {'matricula': matricula})

@admin_required
def delete_matricula(request, id):
    matricula = Matricula.objects.get(id=id)
    matricula.delete()

    return redirect('/matricula/')
# esse crud é para matricula




# esse crud é para professor
@admin_required
def list_professor(request):
    professores = Professor.objects.all()

    return render(request, 'professor/list.html', {
        'professores': professores
    })


@admin_required
def create_professor(request):
    if request.method == 'POST':
        form = ProfessorForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('/professor/')
    else:
        form = ProfessorForm()

    return render(request, 'form.html', {'form': form})


@admin_required
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


@admin_required
def detail_professor(request, id):
    professor = Professor.objects.get(id=id)

    return render(request, 'professor/detail.html', {
        'professor': professor
    })


@admin_required
def delete_professor(request, id):
    professor = Professor.objects.get(id=id)

    professor.delete()

    return redirect('/professor/')

# esse crud é para professor





# esse crud é para turma
@admin_required
def list_turma(request):
    turmas = Turma.objects.all()
    return render(request, 'turma/list.html', {'turmas': turmas})

@admin_required
def create_turma(request):
    if request.method == 'POST':
        form = TurmaForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('/turma/')

    else:
        form = TurmaForm()

    return render(request, 'form.html', {'form': form})

@admin_required
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


@admin_required
def detail_turma(request, id):
    turma = Turma.objects.get(id=id)
    return render(request, 'turma/detail.html', {'turma': turma})

@admin_required
def delete_turma(request, id):
    turma = Turma.objects.get(id=id)
    turma.delete()

    return redirect('/turma/')
# esse crud é para turma