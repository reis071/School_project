from django.test import TestCase, RequestFactory
from django.contrib.auth.models import User
from unittest.mock import patch, Mock
from escolas.views import deletarAluno
from escolas.models import Aluno
from django.shortcuts import reverse, get_object_or_404
from django.http import HttpResponseRedirect

class DeletarAlunoViewTest(TestCase):
    def setUp(self):
        self.factory = RequestFactory()
        self.user = User.objects.create_user(username='unifacs', password='Grc12grc@')
        self.aluno = Aluno.objects.create(id=1, primeiroNome='João', sobrenome='Silva', telefone='12345678901', email='joao.silva@example.com', cpf='12345678901')

    @patch('escolas.views.get_object_or_404')
    @patch('escolas.views.redirect')
    def test_deletarAluno_post(self, mock_redirect, mock_get_object_or_404):
        # Configurando o mock para retornar o aluno criado no setUp
        mock_get_object_or_404.return_value = self.aluno

        # Criando um request mock POST para deletar o aluno
        request = self.factory.post('/deletarAluno/1')

        # Atribuindo usuário ao request (necessário para @login_required)
        request.user = self.user

        # Configurando o mock para retornar um HttpResponseRedirect
        mock_redirect.return_value = HttpResponseRedirect(reverse('alunosCadastrados'))

        # Chamando a view deletarAluno com o request mock
        response = deletarAluno(request, aluno_id=1)

        # Verificando se get_object_or_404 foi chamado corretamente
        mock_get_object_or_404.assert_called_once_with(Aluno, pk=1)

        # Verificando se delete foi chamado no objeto aluno
        self.assertFalse(Aluno.objects.filter(id=1).exists())  # Verificando se o aluno foi deletado

        # Verificando se redirect foi chamado com a URL correta
        mock_redirect.assert_called_once_with('alunosCadastrados')

        # Verificando se a resposta da view é um HttpResponseRedirect
        self.assertIsInstance(response, HttpResponseRedirect)
        self.assertEqual(response.url, reverse('alunosCadastrados'))

    @patch('escolas.views.render')
    @patch('escolas.views.get_object_or_404')
    def test_deletarAluno_get(self, mock_get_object_or_404, mock_render):
        # Configurando o mock para retornar o aluno criado no setUp
        mock_get_object_or_404.return_value = self.aluno

        # Criando um request mock GET para visualizar a página de confirmação de exclusão
        request = self.factory.get('/deletarAluno/1')

        # Atribuindo usuário ao request (necessário para @login_required)
        request.user = self.user

        # Chamando a view deletarAluno com o request mock
        response = deletarAluno(request, aluno_id=1)

        # Verificando se get_object_or_404 foi chamado corretamente
        mock_get_object_or_404.assert_called_once_with(Aluno, pk=1)

        # Verificando se render foi chamado com os parâmetros corretos
        mock_render.assert_called_once_with(
            request,
            'escolas/deletarAluno.html',
            {'aluno': self.aluno}
        )

        # Verificando se a resposta da view é um objeto de renderização
        self.assertEqual(response, mock_render.return_value)
