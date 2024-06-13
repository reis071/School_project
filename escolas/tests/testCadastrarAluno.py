from django.test import TestCase, RequestFactory
from django.contrib.auth.models import User
from unittest.mock import patch, Mock
from escolas.views import cadastrarAluno
from escolas.form import FormAluno
from django.http import HttpResponseRedirect
from django.urls import reverse

class CadastrarAlunoViewTest(TestCase):
    def setUp(self):
        self.factory = RequestFactory()
        self.user = User.objects.create_user(username='unifacs', password='Grc12grc@')

    @patch('escolas.views.FormAluno')
    @patch('escolas.views.render')
    def test_cadastrarAluno_get(self, mock_render, mock_FormAluno):
        # Criação de um request mock
        request = self.factory.get('/cadastrarAluno')
        request.user = self.user

        # Criação de um form mock
        mock_form = Mock(spec=FormAluno)
        mock_FormAluno.return_value = mock_form

        # Chama a função cadastrarAluno com o request mock
        response = cadastrarAluno(request)

        # Verifica se o form foi inicializado corretamente
        mock_FormAluno.assert_called_once_with()

        # Verifica se a função render foi chamada com os parâmetros corretos
        mock_render.assert_called_once_with(
            request,
            'escolas/cadastrarAluno.html',
            {'form': mock_form}
        )

        # Verifica se a resposta da função cadastrarAluno é igual à resposta da função render
        self.assertEqual(response, mock_render.return_value)

    @patch('escolas.views.FormAluno')
    @patch('escolas.views.HttpResponseRedirect')
    @patch('escolas.views.reverse')
    def test_cadastrarAluno_post_valid(self, mock_reverse, mock_HttpResponseRedirect, mock_FormAluno):
        # Criação de um request mock
        request = self.factory.post('/cadastrarAluno', {
            'primeiroNome': 'João',
            'sobrenome': 'Silva',
            'telefone': '12345678901',
            'email': 'joao.silva@example.com',
            'cpf': '12345678901'
        })
        request.user = self.user

        # Criação de um form mock
        mock_form = Mock(spec=FormAluno)
        mock_form.is_valid.return_value = True
        mock_FormAluno.return_value = mock_form

        # Configuração do mock para a função reverse
        mock_reverse.return_value = '/alunosCadastrados/'

        # Configuração do mock para HttpResponseRedirect
        mock_redirect = Mock()
        mock_HttpResponseRedirect.return_value = mock_redirect

        # Chama a função cadastrarAluno com o request mock
        response = cadastrarAluno(request)

        # Verifica se o form foi inicializado corretamente com os dados do POST
        mock_FormAluno.assert_called_once_with(request.POST)

        # Verifica se o método is_valid do form foi chamado
        mock_form.is_valid.assert_called_once()

        # Verifica se o método save do form foi chamado
        mock_form.save.assert_called_once()

        # Verifica se a função reverse foi chamada com o nome correto da URL
        mock_reverse.assert_called_once_with('alunosCadastrados')

        # Verifica se a função HttpResponseRedirect foi chamada com a URL correta
        mock_HttpResponseRedirect.assert_called_once_with('/alunosCadastrados/')

        # Verifica se a resposta da função cadastrarAluno é igual à resposta da função HttpResponseRedirect
        self.assertEqual(response, mock_redirect)

    @patch('escolas.views.FormAluno')
    @patch('escolas.views.render')
    def test_cadastrarAluno_post_invalid(self, mock_render, mock_FormAluno):
        # Criação de um request mock
        request = self.factory.post('/cadastrarAluno', {
            'primeiroNome': 'João',
            'sobrenome': 'Silva',
            'telefone': '12345678901',
            'email': 'joao.silva@example.com',
            'cpf': '12345678901'
        })
        request.user = self.user

        # Criação de um form mock
        mock_form = Mock(spec=FormAluno)
        mock_form.is_valid.return_value = False
        mock_FormAluno.return_value = mock_form

        # Chama a função cadastrarAluno com o request mock
        response = cadastrarAluno(request)

        # Verifica se o form foi inicializado corretamente com os dados do POST
        mock_FormAluno.assert_called_once_with(request.POST)

        # Verifica se o método is_valid do form foi chamado
        mock_form.is_valid.assert_called_once()

        # Verifica se a função render foi chamada com os parâmetros corretos
        mock_render.assert_called_once_with(
            request,
            'escolas/cadastrarAluno.html',
            {'form': mock_form}
        )

        # Verifica se a resposta da função cadastrarAluno é igual à resposta da função render
        self.assertEqual(response, mock_render.return_value)
