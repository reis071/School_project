from django.shortcuts import render, get_object_or_404, redirect  # Importações necessárias
from .form import FormAluno, FormCurso  # Importação dos formulários
from .models import Aluno, Curso  # Importação dos modelos
from django.http import HttpResponseRedirect  # Importação de HttpResponseRedirect
from django.urls import reverse  # Importação de reverse
from django.contrib.auth.decorators import login_required  # Decorador para exigir autenticação

# escolas/views.py

def index(requests):
    """
    View para renderizar a página inicial.
    """
    return render(requests, 'escolas/index.html')

@login_required
def alunosCadastrados(requests):
    """
    View para listar todos os alunos cadastrados.
    Utiliza o decorator @login_required para garantir que apenas usuários autenticados possam acessar.
    """
    alunos = Aluno.objects.order_by('id')
    contexto = {'alunos': alunos}
    return render(requests, 'escolas/alunosCadastrados.html', contexto)

@login_required
def curso(request, idAluno):
    """
    View para exibir os cursos de um aluno específico.
    Utiliza o decorator @login_required para garantir que apenas usuários autenticados possam acessar.
    """
    aluno = get_object_or_404(Aluno, id=idAluno)
    cursos = Curso.objects.filter(aluno=aluno)
    contexto = {'aluno': aluno, 'cursos': cursos}
    return render(request, 'escolas/curso.html', contexto)

@login_required
def cadastrarAluno(requests):
    """
    View para cadastrar um novo aluno.
    Utiliza o decorator @login_required para garantir que apenas usuários autenticados possam acessar.
    """
    if requests.method != 'POST':
        form = FormAluno()
    else:
        form = FormAluno(requests.POST)
        
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('alunosCadastrados'))
    
    contexto = {'form': form}
    return render(requests, 'escolas/cadastrarAluno.html', contexto)

@login_required
def editarAluno(request, aluno_id):
    """
    View para editar os dados de um aluno existente.
    Utiliza o decorator @login_required para garantir que apenas usuários autenticados possam acessar.
    """
    aluno = get_object_or_404(Aluno, pk=aluno_id)
    
    if request.method == 'POST':
        form = FormAluno(request.POST, instance=aluno)
        if form.is_valid():
            form.save()
            return redirect('alunosCadastrados')
    else:
        form = FormAluno(instance=aluno)
    
    return render(request, 'escolas/editarAluno.html', {'form': form, 'aluno': aluno})

@login_required
def deletarAluno(request, aluno_id):
    """
    View para deletar um aluno existente.
    Utiliza o decorator @login_required para garantir que apenas usuários autenticados possam acessar.
    """
    aluno = get_object_or_404(Aluno, pk=aluno_id)
    
    if request.method == 'POST':
        aluno.delete()
        return redirect('alunosCadastrados')
    
    return render(request, 'escolas/deletarAluno.html', {'aluno': aluno})

@login_required
def cadastrarCurso(requests, idAluno):
    """
    View para cadastrar um novo curso para um aluno específico.
    Utiliza o decorator @login_required para garantir que apenas usuários autenticados possam acessar.
    """
    aluno = Aluno.objects.get(id=idAluno)
    
    if requests.method != 'POST':
        form = FormCurso()
    else:
        form = FormCurso(requests.POST)
        
        if form.is_valid():
            novoCurso = form.save(commit=False)
            novoCurso.aluno = aluno
            novoCurso.save()
            return HttpResponseRedirect(reverse('curso', args=[idAluno]))
            
    contexto = {'aluno': aluno, 'form': form}
    
    return render(requests, 'escolas/cadastrarCurso.html', contexto)

@login_required
def deletarCurso(request, idCurso):
    """
    View para deletar um curso existente de um aluno.
    Utiliza o decorator @login_required para garantir que apenas usuários autenticados possam acessar.
    """
    curso = get_object_or_404(Curso, id=idCurso)
    aluno_id = curso.aluno.id
    
    if request.method == 'POST':
        curso.delete()
        return redirect('curso', idAluno=aluno_id)
    
    return render(request, 'escolas/deletarCurso.html', {'curso': curso})

@login_required
def editarCurso(requests, idCurso):
    """
    View para editar um curso existente de um aluno.
    Utiliza o decorator @login_required para garantir que apenas usuários autenticados possam acessar.
    """
    cursos = Curso.objects.get(id=idCurso)
    aluno = cursos.aluno

    if requests.method != 'POST':
        form = FormCurso(instance=cursos)
    else:
        form = FormCurso(instance=cursos, data=requests.POST)
        
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('curso', args=[aluno.id]))
        
    contexto = {'cursos': cursos, 'aluno': aluno, 'form': form}
    
    return render(requests, 'escolas/editarCurso.html', contexto)
