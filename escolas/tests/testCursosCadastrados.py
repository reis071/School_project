from django.test import TestCase, RequestFactory
from unittest.mock import patch, Mock
from django.contrib.auth.models import User
from escolas.views import curso
from escolas.models import Aluno, Curso

class CursoViewTest(TestCase):
    def setUp(self):
        self.factory = RequestFactory()
        self.user = User.objects.create_user(username='unifacs', password='Grc12grc@')
        self.aluno = Aluno.objects.create(id=1, primeiroNome='João', sobrenome='Silva')

    @patch('escolas.views.get_object_or_404')
    @patch('escolas.views.Curso.objects.filter')
    @patch('escolas.views.render')
    def test_curso(self, mock_render, mock_filter, mock_get_object_or_404):
        
        # Criação de objetos mock para cursos
        mock_curso1 = Mock()
        mock_curso1.id = 1
        mock_curso1.nome = 'Curso A'

        mock_curso2 = Mock()
        mock_curso2.id = 2
        mock_curso2.nome = 'Curso B'

        # Configuração do mock para retornar o aluno mockado
        mock_get_object_or_404.return_value = self.aluno

        # Configuração do mock para retornar uma lista de cursos mock quando chamado
        mock_filter.return_value = [mock_curso1, mock_curso2]

        # Criação de um request mock
        request = self.factory.get('/curso/1')

        # Autenticando o usuário no request
        request.user = self.user

        # Chama a função curso com o request mock e o id do aluno
        response = curso(request, idAluno=1)

        # Verifica se a função get_object_or_404 foi chamada corretamente
        mock_get_object_or_404.assert_called_once_with(Aluno, id=1)

        # Verifica se a função filter foi chamada corretamente
        mock_filter.assert_called_once_with(aluno=self.aluno)

        # Verifica se a função render foi chamada com os parâmetros corretos
        mock_render.assert_called_once_with(
            request,
            'escolas/curso.html',
            {'aluno': self.aluno, 'cursos': [mock_curso1, mock_curso2]}
        )

        # Verifica se a resposta da função curso é igual à resposta da função render
        self.assertEqual(response, mock_render.return_value)
