# Generated by Django 4.0.2 on 2022-02-18 00:30

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('Cadastro', '0003_cliente_foto'),
    ]

    operations = [
        migrations.AddField(
            model_name='cliente',
            name='criado',
            field=models.DateField(auto_now_add=True, default=datetime.datetime(2022, 2, 18, 0, 30, 9, 699594, tzinfo=utc)),
            preserve_default=False,
        ),
    ]
