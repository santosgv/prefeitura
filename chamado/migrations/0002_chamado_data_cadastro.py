# Generated by Django 4.2.3 on 2023-08-10 13:56

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chamado', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='chamado',
            name='data_cadastro',
            field=models.DateField(default=datetime.date.today),
        ),
    ]
