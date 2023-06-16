# Generated by Django 4.2.2 on 2023-06-08 20:51

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('usuarios', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=50)),
                ('descricao', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Livros',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img', models.FileField(blank=True, null=True, upload_to='capa_livro')),
                ('nome', models.CharField(max_length=80)),
                ('autor', models.CharField(max_length=30)),
                ('co_autor', models.CharField(blank=True, max_length=30, null=True)),
                ('data_cadastro', models.DateField(default=datetime.date.today, null=True)),
                ('esta_emprestado', models.BooleanField(default=False, editable=False)),
                ('quantidade', models.PositiveIntegerField(default=1)),
                ('categoria', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='livro.categoria')),
            ],
            options={
                'verbose_name': 'Livro',
            },
        ),
        migrations.CreateModel(
            name='Emprestimos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome_emprestado', models.CharField(blank=True, max_length=120, null=True)),
                ('data_emprestimo', models.DateField(blank=True, default=datetime.date.today, null=True)),
                ('data_devolucao', models.DateField(blank=True, null=True)),
                ('tempo_duracao', models.DurationField(blank=True, null=True)),
                ('esta_emprestado', models.BooleanField(default=False)),
                ('emprestado', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='livro.livros')),
                ('nome_turma', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='usuarios.turma')),
                ('usuario', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='usuarios.usuario')),
            ],
            options={
                'verbose_name': 'Emprestimo',
            },
        ),
    ]
