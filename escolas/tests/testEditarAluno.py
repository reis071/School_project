from django.test import TestCase, RequestFactory
from django.contrib.auth.models import User
from unittest.mock import patch, Mock
from escolas.views import editarAluno
from escolas.models import Aluno
from escolas.form import FormAluno
from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse

class EditarAlunoViewTest(TestCase):
    def setUp(self):
        self.factory = RequestFactory()
        self.user = User.objects.create_user(username='unifacs', password='Grc12grc@')
        self.aluno = Aluno.objects.create(id=1, primeiroNome='João', sobrenome='Silva', telefone='12345678901', email='joao.silva@example.com', cpf='12345678901')

    @patch('escolas.views.FormAluno')
    @patch('escolas.views.render')
    @patch('escolas.views.get_object_or_404')
    def test_editarAluno_get(self, mock_get_object_or_404, mock_render, mock_FormAluno):
        # Configuração do mock para retornar o aluno mockado
        mock_get_object_or_404.return_value = self.aluno

        # Criação de um request mock
        request = self.factory.get('/editarAluno/1')
        request.user = self.user

        # Criação de um form mock
        mock_form = Mock(spec=FormAluno)
        mock_FormAluno.return_value = mock_form

        # Chama a função editarAluno com o request mock e o id do aluno
        response = editarAluno(request, aluno_id=1)

        # Verifica se a função get_object_or_404 foi chamada corretamente
        mock_get_object_or_404.assert_called_once_with(Aluno, pk=1)

        # Verifica se o form foi inicializado corretamente
        mock_FormAluno.assert_called_once_with(instance=self.aluno)

        # Verifica se a função render foi chamada com os parâmetros corretos
        mock_render.assert_called_once_with(
            request,
            'escolas/editarAluno.html',
            {'form': mock_form, 'aluno': self.aluno}
        )

        # Verifica se a resposta da função editarAluno é igual à resposta da função render
        self.assertEqual(response, mock_render.return_value)

    @patch('escolas.views.FormAluno')
    @patch('escolas.views.redirect')
    @patch('escolas.views.get_object_or_404')
    def test_editarAluno_post_valid(self, mock_get_object_or_404, mock_redirect, mock_FormAluno):
        # Configuração do mock para retornar o aluno mockado
        mock_get_object_or_404.return_value = self.aluno

        # Criação de um request mock
        request = self.factory.post('/editarAluno/1', {
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

        # Chama a função editarAluno com o request mock e o id do aluno
        response = editarAluno(request, aluno_id=1)

        # Verifica se a função get_object_or_404 foi chamada corretamente
        mock_get_object_or_404.assert_called_once_with(Aluno, pk=1)

        # Verifica se o form foi inicializado corretamente com os dados do POST e a instância do aluno
        mock_FormAluno.assert_called_once_with(request.POST, instance=self.aluno)

        # Verifica se o método is_valid do form foi chamado
        mock_form.is_valid.assert_called_once()

        # Verifica se o método save do form foi chamado
        mock_form.save.assert_called_once()

        # Verifica se a função redirect foi chamada com o nome correto da URL
        mock_redirect.assert_called_once_with('alunosCadastrados')

        # Verifica se a resposta da função editarAluno é igual à resposta da função redirect
        self.assertEqual(response, mock_redirect.return_value)

    @patch('escolas.views.FormAluno')
    @patch('escolas.views.render')
    @patch('escolas.views.get_object_or_404')
    def test_editarAluno_post_invalid(self, mock_get_object_or_404, mock_render, mock_FormAluno):
        # Configuração do mock para retornar o aluno mockado
        mock_get_object_or_404.return_value = self.aluno

        # Criação de um request mock
        request = self.factory.post('/editarAluno/1', {
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

        # Chama a função editarAluno com o request mock e o id do aluno
        response = editarAluno(request, aluno_id=1)

        # Verifica se a função get_object_or_404 foi chamada corretamente
        mock_get_object_or_404.assert_called_once_with(Aluno, pk=1)

        # Verifica se o form foi inicializado corretamente com os dados do POST e a instância do aluno
        mock_FormAluno.assert_called_once_with(request.POST, instance=self.aluno)

        # Verifica se o método is_valid do form foi chamado
        mock_form.is_valid.assert_called_once()

        # Verifica se a função render foi chamada com os parâmetros corretos
        mock_render.assert_called_once_with(
            request,
            'escolas/editarAluno.html',
            {'form': mock_form, 'aluno': self.aluno}
        )

        # Verifica se a resposta da função editarAluno é igual à resposta da função render
        self.assertEqual(response, mock_render.return_value)
