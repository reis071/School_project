from django import forms
from .models import Aluno,Curso

class FormAluno(forms.ModelForm):
    class Meta:
        model = Aluno
        fields = ['primeiroNome','sobrenome','telefone','email','cpf']

class FormCurso(forms.ModelForm):
    class Meta:
        model = Curso
        fields = ['nomeCurso', 'valor', 'parcelas', 'dataInicioCurso', 'dataFimCurso']