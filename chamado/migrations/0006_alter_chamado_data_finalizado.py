# Generated by Django 4.2.3 on 2023-08-14 15:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chamado', '0005_chamado_data_finalizado'),
    ]

    operations = [
        migrations.AlterField(
            model_name='chamado',
            name='data_finalizado',
            field=models.CharField(default='--', max_length=12),
        ),
    ]
