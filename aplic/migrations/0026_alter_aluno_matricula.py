# Generated by Django 4.2.6 on 2023-10-15 18:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aplic', '0025_instituicao_endereco_instituicao_telefone_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='aluno',
            name='matricula',
            field=models.IntegerField(default=22348, unique=True, verbose_name='Matrícula'),
        ),
    ]