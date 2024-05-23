# escolas/tests.py

# escolas/tests.py

from django.test import TestCase, Client
from django.urls import reverse
from unittest.mock import patch, MagicMock
from .models import Aluno, Curso
from .form import FormAluno, FormCurso

'''class ViewsTestCase(TestCase):
    def setUp(self):
        self.client = Client()

    def test_index_view(self):
        response = self.client.get(reverse('index'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'escolas/index.html')

    @patch('escolas.views.Aluno.objects.order_by')
    def test_alunosCadastrados_view(self, mock_order_by):
        mock_order_by.return_value = []
        response = self.client.get(reverse('alunosCadastrados'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'escolas/alunosCadastrados.html')
        mock_order_by.assert_called_once_with('id')

    @patch('escolas.views.get_object_or_404')
    @patch('escolas.views.Curso.objects.filter')
    def test_curso_view(self, mock_filter, mock_get_object_or_404):
        mock_aluno = Aluno(id=1, primeiroNome='John', sobrenome='Doe', telefone='12345678901', email='john.doe@example.com', cpf='12345678901')
        mock_get_object_or_404.return_value = mock_aluno
        mock_filter.return_value = []

        response = self.client.get(reverse('curso', args=[1]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'escolas/curso.html')
        mock_get_object_or_404.assert_called_once_with(Aluno, id=1)
        mock_filter.assert_called_once_with(aluno=mock_aluno)

    @patch('escolas.views.FormAluno')
    def test_cadastrarAluno_view_get(self, mock_form):
        mock_form.return_value = MagicMock()
        response = self.client.get(reverse('cadastrarAluno'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'escolas/cadastrarAluno.html')
        mock_form.assert_called_once()

    @patch('escolas.views.FormAluno')
    def test_cadastrarAluno_view_post(self, mock_form):
        mock_form_instance = mock_form.return_value
        mock_form_instance.is_valid.return_value = True
        mock_form_instance.save.return_value = None

        response = self.client.post(reverse('cadastrarAluno'), data={
            'primeiroNome': 'John',
            'sobrenome': 'Doe',
            'telefone': '12345678901',
            'email': 'john.doe@example.com',
            'cpf': '12345678901'
        })

        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse('alunosCadastrados'))
        mock_form_instance.is_valid.assert_called_once()
        mock_form_instance.save.assert_called_once()

    @patch('escolas.views.FormCurso')
    @patch('escolas.views.Aluno.objects.get')
    def test_cadastrarCurso_view_post(self, mock_get, mock_form):
        mock_aluno = Aluno(id=1, primeiroNome='John', sobrenome='Doe', telefone='12345678901', email='john.doe@example.com', cpf='12345678901')
        mock_get.return_value = mock_aluno
        mock_form_instance = mock_form.return_value
        mock_form_instance.is_valid.return_value = True
        mock_form_instance.save.return_value = MagicMock()

        response = self.client.post(reverse('cadastrarCurso', args=[1]), data={
            'nomeCurso': 'Python',
            'valor': 100.0,
            'parcelas': 10,
            'dataInicioCurso': '2024-05-22',
            'dataFimCurso': '2024-05-23'
        })

        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse('curso', args=[1]))
        mock_get.assert_called_once_with(id=1)
        mock_form_instance.is_valid.assert_called_once()
        mock_form_instance.save.assert_called_once()
        self.assertEqual(mock_form_instance.save.call_args[1]['commit'], False)

    @patch('escolas.views.FormCurso')
    @patch('escolas.views.Curso.objects.get')
    def test_editarCurso_view_post(self, mock_get, mock_form):
        mock_curso = Curso(id=1, nomeCurso='Python', valor=100.0, parcelas=10, dataInicioCurso='2024-05-22', dataFimCurso='2024-05-23')
        mock_curso.aluno = Aluno(id=1, primeiroNome='John', sobrenome='Doe', telefone='12345678901', email='john.doe@example.com', cpf='12345678901')
        mock_get.return_value = mock_curso
        mock_form_instance = mock_form.return_value
        mock_form_instance.is_valid.return_value = True

        response = self.client.post(reverse('editarCurso', args=[1]), data={
            'nomeCurso': 'Python',
            'valor': 100.0,
            'parcelas': 10,
            'dataInicioCurso': '2024-05-22',
            'dataFimCurso': '2024-05-23'
        })

        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse('curso', args=[mock_curso.aluno.id]))
        mock_get.assert_called_once_with(id=1)
        mock_form_instance.is_valid.assert_called_once()
        mock_form_instance.save.assert_called_once()
'''

''''class AlunoModelTest(TestCase):
    @patch('escolas.models.Aluno.save', autospec=True)
    def test_create_aluno(self, mock_save):
        aluno = Aluno(primeiroNome='John', sobrenome='Doe', telefone='12345678901', email='john.doe@example.com', cpf='12345678901')
        aluno.save()
        mock_save.assert_called_once()

    @patch('escolas.models.Curso.save', autospec=True)
    def test_create_curso(self, mock_save):
        aluno = Aluno(primeiroNome='John', sobrenome='Doe', telefone='12345678901', email='john.doe@example.com', cpf='12345678901')
        aluno.save()
        curso = Curso(aluno=aluno, nomeCurso='Python', valor=100.0, parcelas=10, dataInicioCurso=timezone.now(), dataFimCurso=timezone.now())
        curso.save()
        mock_save.assert_called_once()'''
