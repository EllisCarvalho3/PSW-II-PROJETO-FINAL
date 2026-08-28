from django.contrib import admin
from django.urls import path, include
from core import views

urlpatterns = [
    path('admin/', admin.site.urls),
    
    path('accounts/', include('django.contrib.auth.urls')),

    path('', views.index, name='index'),

    path('aluno/', views.list_aluno, name='list_aluno'),
    path('aluno/criar/', views.create_aluno, name='create_aluno'),
    path('aluno/atualizar/<int:id>/', views.update_aluno, name='update_aluno'),
    path('aluno/deletar/<int:id>/', views.delete_aluno, name='delete_aluno'),
    path('aluno/detalhes/<int:id>/', views.detail_aluno, name='detail_aluno'),
    
    path('instrumento/', views.list_instrumento, name='list_instrumento'),
    path('instrumento/criar/', views.create_instrumento, name='create_instrumento'),
    path('instrumento/atualizar/<int:id>/', views.update_instrumento, name='update_instrumento'),
    path('instrumento/deletar/<int:id>/', views.delete_instrumento, name='delete_instrumento'),
    path('instrumento/detalhes/<int:id>/', views.detail_instrumento, name='detail_instrumento'),
    
    path('matricula/', views.list_matricula, name='list_matricula'),
    path('matricula/criar/', views.create_matricula, name='create_matricula'),
    path('matricula/atualizar/<int:id>/', views.update_matricula, name='update_matricula'),
    path('matricula/deletar/<int:id>/', views.delete_matricula, name='delete_matricula'),
    path ('matricula/detalhes/<int:id>/', views.detail_matricula, name='detail_matricula'),
    
    path('professor/', views.list_professor, name='list_professor'),
    path('professor/criar/', views.create_professor, name='create_professor'),
    path('professor/atualizar/<int:id>/', views.update_professor, name='update_professor'),
    path('professor/deletar/<int:id>/', views.delete_professor, name='delete_professor'),
    path('professor/detalhes/<int:id>/', views.detail_professor, name='detail_professor'),
    
    path('turma/', views.list_turma, name='list_turma'),
    path('turma/criar/', views.create_turma, name='create_turma'),
    path('turma/atualizar/<int:id>/', views.update_turma, name='update_turma'),
    path('turma/deletar/<int:id>/', views.delete_turma, name='delete_turma'),
    path('turma/detalhes/<int:id>/', views.detail_turma, name='detail_turma'),
]