# Generated by Django 4.0.2 on 2022-02-17 06:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Cadastro', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cliente',
            name='cpf',
            field=models.CharField(max_length=11, unique=True),
        ),
        migrations.AlterField(
            model_name='cliente',
            name='telefone',
            field=models.CharField(max_length=11, unique=True),
        ),
    ]
