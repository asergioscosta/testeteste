# Generated by Django 4.2.6 on 2023-10-15 18:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('aplic', '0036_alter_aluno_matricula_alter_equipe_projeto'),
    ]

    operations = [
        migrations.AlterField(
            model_name='aluno',
            name='matricula',
            field=models.IntegerField(default=96974, unique=True, verbose_name='Matrícula'),
        ),
        migrations.AlterField(
            model_name='equipe',
            name='aluno',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='aplic.aluno'),
        ),
    ]