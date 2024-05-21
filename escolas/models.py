from django.db import models
from django.utils import timezone

# Create your models here.
class Aluno(models.Model):
    primeiroNome = models.CharField(max_length=50)
    sobrenome = models.CharField(max_length=80)
    telefone = models.CharField(max_length=11) 
    email = models.CharField(max_length=60,unique=True) 
    cpf = models.CharField(max_length=11,unique=True) 
    
class Curso(models.Model):
    aluno = models.ForeignKey(Aluno,on_delete=models.CASCADE)
    nomeCurso = models.CharField(max_length=20)
    valor = models.FloatField() 
    parcelas = models.IntegerField() 
    dataInicioCurso = models.DateField(default=timezone.now)
    dataFimCurso = models.DateField(default=timezone.now)
    