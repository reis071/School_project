"""
URL configuration for horse project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('alunosCadastrados', views.alunosCadastrados, name='alunosCadastrados'),
    path('curso/<idAluno>/', views.curso, name='curso'),
    path('cadastrarAluno', views.cadastrarAluno, name='cadastrarAluno'),
    path('cadastrarCurso/<idAluno>', views.cadastrarCurso, name='cadastrarCurso'),
    path('editarCurso/<idCurso>', views.editarCurso, name='editarCurso'),
]