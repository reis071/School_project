from django.test import TestCase, RequestFactory
from unittest.mock import patch, Mock
from django.http import HttpRequest
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from escolas.views import alunosCadastrados

class AlunosCadastradosViewTest(TestCase):
    def setUp(self):
        self.factory = RequestFactory()
        self.user = User.objects.create_user(username='unifacs', password='Grc12grc@')

    @patch('escolas.views.Aluno.objects.order_by')  # Configuração do mock para order_by
    @patch('escolas.views.render')  # Configuração do mock para render
    def test_alunosCadastrados(self, mock_render, mock_order_by):
        
        # Criação de objetos mock para alunos
        mock_aluno1 = Mock()
        mock_aluno1.id = 1
        mock_aluno1.primeiroNome = 'João'
        mock_aluno1.sobrenome = 'Silva'
        mock_aluno1.telefone = '12345678901'
        mock_aluno1.email = 'joao.silva@example.com'
        mock_aluno1.cpf = '12345678901'

        mock_aluno2 = Mock()
        mock_aluno2.id = 2
        mock_aluno2.primeiroNome = 'Maria'
        mock_aluno2.sobrenome = 'Oliveira'
        mock_aluno2.telefone = '10987654321'
        mock_aluno2.email = 'maria.oliveira@example.com'
        mock_aluno2.cpf = '10987654321'

        # Configuração do mock para retornar uma lista de alunos mock quando chamado
        mock_order_by.return_value = [mock_aluno1, mock_aluno2]

        # Criação de um request mock
        request = self.factory.get('/alunosCadastrados')

        # Autenticando o usuário no request
        request.user = self.user

        # Chama a função alunosCadastrados com o request mock
        response = alunosCadastrados(request)

        # Verifica se a função order_by foi chamada corretamente
        mock_order_by.assert_called_once_with('id')

        # Verifica se a função render foi chamada com os parâmetros corretos
        mock_render.assert_called_once_with(
            request,
            'escolas/alunosCadastrados.html',
            {'alunos': [mock_aluno1, mock_aluno2]}
        )

        # Verifica se a resposta da função alunosCadastrados é igual à resposta da função render
        self.assertEqual(response, mock_render.return_value)
