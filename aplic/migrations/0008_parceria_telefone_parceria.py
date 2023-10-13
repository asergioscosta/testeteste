# Generated by Django 4.2.6 on 2023-10-08 13:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('aplic', '0007_remove_telefone_parceria_delete_parceria'),
    ]

    operations = [
        migrations.CreateModel(
            name='Parceria',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome_parceria', models.CharField(max_length=10, verbose_name='Nome da Parceria')),
                ('cnpj', models.CharField(max_length=11, verbose_name='CNPJ')),
                ('email', models.EmailField(blank=True, max_length=200, verbose_name='E-mail')),
            ],
            options={
                'verbose_name': 'Parceria',
                'verbose_name_plural': 'Parcerias',
            },
        ),
        migrations.AddField(
            model_name='telefone',
            name='parceria',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='aplic.parceria'),
            preserve_default=False,
        ),
    ]