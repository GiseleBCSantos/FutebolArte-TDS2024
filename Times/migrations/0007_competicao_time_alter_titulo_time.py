# Generated by Django 4.2 on 2024-02-28 14:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Times', '0006_alter_jogador_foto_alter_time_divisao_atual'),
    ]

    operations = [
        migrations.AddField(
            model_name='competicao',
            name='time',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='Competicoes', to='Times.time'),
        ),
        migrations.AlterField(
            model_name='titulo',
            name='time',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Titulos', to='Times.time'),
        ),
    ]