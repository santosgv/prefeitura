# Generated by Django 4.2.3 on 2023-08-16 04:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chamado', '0010_chamado_solucao'),
    ]

    operations = [
        migrations.AlterField(
            model_name='chamado',
            name='data_finalizado',
            field=models.DateField(blank=True, null=True),
        ),
    ]
