# Generated by Django 4.2.3 on 2023-07-26 02:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='usuario',
            name='local',
            field=models.CharField(default='N/A', max_length=65),
        ),
    ]
