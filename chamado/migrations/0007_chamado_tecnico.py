# Generated by Django 4.2.3 on 2023-08-15 13:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('logadm', '0002_rename_usuario_usuarioa'),
        ('chamado', '0006_alter_chamado_data_finalizado'),
    ]

    operations = [
        migrations.AddField(
            model_name='chamado',
            name='tecnico',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.DO_NOTHING, to='logadm.usuarioa'),
            preserve_default=False,
        ),
    ]
