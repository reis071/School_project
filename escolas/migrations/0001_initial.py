import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Aluno',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('primeiroNome', models.CharField(max_length=50)),
                ('sobrenome', models.CharField(max_length=80)),
                ('telefone', models.CharField(max_length=11)),
                ('cpf', models.CharField(max_length=11)),
            ],
        ),
        migrations.CreateModel(
            name='Curso',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nomeCurso', models.CharField(max_length=20)),
                ('valor', models.FloatField()),
                ('parcelas', models.IntegerField()),
                ('dataIncioCurso', models.DateField()),
                ('aluno', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='escolas.aluno')),
            ],
        ),
    ]
