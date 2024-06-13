from django.test import TestCase, RequestFactory
from django.contrib.auth.models import User
from unittest.mock import patch, Mock
from escolas.views import deletarCurso
from escolas.models import Aluno, Curso
from django.shortcuts import reverse, get_object_or_404
from django.http import HttpResponseRedirect

class DeletarCursoViewTest(TestCase):
    def setUp(self):
        self.factory = RequestFactory()
        self.user = User.objects.create_user(username='unifacs', password='Grc12grc@')
        self.aluno = Aluno.objects.create(id=1, primeiroNome='João', sobrenome='Silva', telefone='12345678901', email='joao.silva@example.com', cpf='12345678901')
        self.curso = Curso.objects.create(id=1, aluno=self.aluno, nomeCurso='Curso A', valor=100.0, parcelas=12)

    @patch('escolas.views.get_object_or_404')
    @patch('escolas.views.redirect')
    def test_deletarCurso_post(self, mock_redirect, mock_get_object_or_404):
        # Configurando o mock para retornar o curso criado no setUp
        mock_get_object_or_404.return_value = self.curso

        # Criando um request mock POST para deletar o curso
        request = self.factory.post('/deletarCurso/1')

        # Atribuindo usuário ao request (necessário para @login_required)
        request.user = self.user

        # Configurando o mock para retornar um HttpResponseRedirect
        mock_redirect.return_value = HttpResponseRedirect(reverse('curso', args=[self.aluno.id]))

        # Chamando a view deletarCurso com o request mock
        response = deletarCurso(request, idCurso=1)

        # Verificando se get_object_or_404 foi chamado corretamente
        mock_get_object_or_404.assert_called_once_with(Curso, id=1)

        # Verificando se delete foi chamado no objeto curso
        self.assertFalse(Curso.objects.filter(id=1).exists())  # Verificando se o curso foi deletado

        # Verificando se redirect foi chamado com a URL correta
        mock_redirect.assert_called_once_with('curso', idAluno=self.aluno.id)

        # Verificando se a resposta da view é um HttpResponseRedirect
        self.assertIsInstance(response, HttpResponseRedirect)
        self.assertEqual(response.url, reverse('curso', args=[self.aluno.id]))

    @patch('escolas.views.render')
    @patch('escolas.views.get_object_or_404')
    def test_deletarCurso_get(self, mock_get_object_or_404, mock_render):
        # Configurando o mock para retornar o curso criado no setUp
        mock_get_object_or_404.return_value = self.curso

        # Criando um request mock GET para visualizar a página de confirmação de exclusão
        request = self.factory.get('/deletarCurso/1')

        # Atribuindo usuário ao request (necessário para @login_required)
        request.user = self.user

        # Chamando a view deletarCurso com o request mock
        response = deletarCurso(request, idCurso=1)

        # Verificando se get_object_or_404 foi chamado corretamente
        mock_get_object_or_404.assert_called_once_with(Curso, id=1)

        # Verificando se render foi chamado com os parâmetros corretos
        mock_render.assert_called_once_with(
            request,
            'escolas/deletarCurso.html',
            {'curso': self.curso}
        )

        # Verificando se a resposta da view é um objeto de renderização
        self.assertEqual(response, mock_render.return_value)
