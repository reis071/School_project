from django.test import TestCase, RequestFactory
from django.contrib.auth.models import User
from unittest.mock import patch, Mock
from escolas.views import editarCurso
from escolas.models import Aluno, Curso
from escolas.form import FormCurso  
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.utils import timezone

class EditarCursoViewTest(TestCase):
    def setUp(self):
        self.factory = RequestFactory()
        self.user = User.objects.create_user(username='unifacs', password='Grc12grc@')
        self.aluno = Aluno.objects.create(id=1, primeiroNome='João', sobrenome='Silva', telefone='12345678901', email='joao.silva@example.com', cpf='12345678901')
        self.curso = Curso.objects.create(id=1, aluno=self.aluno, nomeCurso='Curso A', valor=100.0, parcelas=12)

    @patch('escolas.views.FormCurso')
    @patch('escolas.views.render')
    @patch('escolas.views.reverse')
    @patch('escolas.views.HttpResponseRedirect')
    def test_editarCurso_post_valid(self, mock_HttpResponseRedirect, mock_reverse, mock_render, mock_FormCurso):
        # Criação de um request mock
        request = self.factory.post('/editarCurso/1', {
            'nomeCurso': 'Novo Curso',
            'valor': 200.0,
            'parcelas': 6,
            'dataInicioCurso': '2023-01-01',
            'dataFimCurso': '2023-06-30',
        })
        request.user = self.user

        # Criação de um form mock
        mock_form = Mock(spec=FormCurso)
        mock_form.is_valid.return_value = True
        mock_FormCurso.return_value = mock_form

        # Configuração do mock para a função reverse
        mock_reverse.return_value = '/curso/1/'

        # Configuração do mock para HttpResponseRedirect
        mock_redirect = Mock()
        mock_HttpResponseRedirect.return_value = mock_redirect

        # Chama a função editarCurso com o request mock
        response = editarCurso(request, idCurso=1)

        # Verifica se o form foi inicializado corretamente com os dados do POST e a instância do curso
        mock_FormCurso.assert_called_once_with(
            instance=self.curso,
            data=request.POST  # Alterado para request.POST
        )

        # Verifica se o método is_valid do form foi chamado
        mock_form.is_valid.assert_called_once()

        # Verifica se o método save do form foi chamado
        mock_form.save.assert_called_once()

        # Verifica se a função reverse foi chamada com o nome correto da URL
        mock_reverse.assert_called_once_with('curso', args=[1])

        # Verifica se a função HttpResponseRedirect foi chamada com a URL correta
        mock_HttpResponseRedirect.assert_called_once_with('/curso/1/')

        # Verifica se a resposta da função editarCurso é igual à resposta da função HttpResponseRedirect
        self.assertEqual(response, mock_redirect)
