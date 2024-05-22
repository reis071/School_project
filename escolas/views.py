from django.shortcuts import render,get_object_or_404
from .form import FormAluno,FormCurso
from .models import Aluno,Curso
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required

# Create your views here.

def index(requests):
    return render(requests,'escolas/index.html')

@login_required
def alunosCadastrados(requests):
    alunos = Aluno.objects.order_by('id')
    contexto = {'alunos':alunos}
    return render(requests,'escolas/alunosCadastrados.html',contexto)

@login_required
def curso(request, idAluno):
    aluno = get_object_or_404(Aluno, id=idAluno)
    cursos = Curso.objects.filter(aluno=aluno)
    contexto = {'aluno': aluno, 'cursos': cursos}
    return render(request, 'escolas/curso.html', contexto)

@login_required
def cadastrarAluno(requests):
    if requests.method != 'POST':
        form = FormAluno()
    else:
        form = FormAluno(requests.POST)
        
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('alunosCadastrados'))
    
    contexto = {'form':form}
    return render(requests,'escolas/cadastrarAluno.html',contexto)

@login_required
def cadastrarCurso(requests, idAluno):
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
            
    contexto = {'aluno':aluno, 'form':form}
    
    return render(requests,'escolas/cadastrarCurso.html',contexto)

@login_required
def editarCurso(requests,idCurso):
    cursos = Curso.objects.get(id=idCurso)
    aluno = cursos.aluno

    if requests.method != 'POST':
        form = FormCurso(instance=cursos)
    else:
        form = FormCurso(instance=cursos, data=requests.POST)
        
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('curso', args=[aluno.id]))
        
    contexto = {'cursos':cursos,'aluno':aluno,'form':form}
    
    return render(requests,'escolas/editarCurso.html',contexto)