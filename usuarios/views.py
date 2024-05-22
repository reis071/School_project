
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth import logout,authenticate,login
from django.contrib.auth.forms import UserCreationForm

def logout_view(requests):
    logout(requests)
    return HttpResponseRedirect(reverse('index'))


def register(request):
    if request.method != 'POST':
        form = UserCreationForm()
    else:
        form = UserCreationForm(data = request.POST)
        
        if form.is_valid():
            novo_usuario = form.save()
            usuario_cadastrado = authenticate(username = novo_usuario.username, password = request.POST['password1'])
            return HttpResponseRedirect(reverse('index'))
    
    contexto = {'form':form}
    return render(request, 'usuarios/register.html', contexto)
            
# Create your views here.
