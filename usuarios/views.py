from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from .form import FormLogin
from django.contrib.auth import authenticate
from django.contrib.auth import login as autUser

def login(requests):
    if requests.method != 'POST':
        form = FormLogin()
    else:
        form = FormLogin(data=requests.POST)
        
        if form.is_valid():
            username = requests.POST.get('username')
            password = requests.POST.get('password')
            validarUsuario = authenticate(username=username,password=password)
            
            if validarUsuario:
                autUser(requests,validarUsuario)
                HttpResponseRedirect(reverse('index'))
        
        contexto = {'form':form}
        
        return render(requests,'escolas/login.html',contexto)
            
            
# Create your views here.
