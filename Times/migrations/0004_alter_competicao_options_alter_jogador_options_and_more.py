# Generated by Django 4.2 on 2024-02-28 13:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Times', '0003_alter_time_escudo_titulo'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='competicao',
            options={'verbose_name': 'Competição', 'verbose_name_plural': 'Competições'},
        ),
        migrations.AlterModelOptions(
            name='jogador',
            options={'verbose_name': 'Jogador', 'verbose_name_plural': 'Jogadores'},
        ),
        migrations.AlterModelOptions(
            name='time',
            options={'verbose_name': 'Clube', 'verbose_name_plural': 'Clubes'},
        ),
        migrations.AlterModelOptions(
            name='titulo',
            options={'verbose_name': 'Título', 'verbose_name_plural': 'Títulos'},
        ),
        migrations.RemoveField(
            model_name='time',
            name='pais',
        ),
        migrations.RemoveField(
            model_name='time',
            name='uf',
        ),
        migrations.AlterField(
            model_name='jogador',
            name='foto',
            field=models.ImageField(upload_to='Times/Jogadores'),
        ),
        migrations.AlterField(
            model_name='jogador',
            name='posicao',
            field=models.CharField(choices=[('Goleiro', 'Goleiro'), ('Zagueiro', 'Zagueiro'), ('Lateral', 'Lateral'), ('Atacante', 'Atacante')], max_length=20),
        ),
        migrations.AlterField(
            model_name='time',
            name='divisao_atual',
            field=models.CharField(choices=[('A', 'Série A'), ('B', 'Série B'), ('C', 'Série C'), ('D', 'Série D'), ('S', 'Sem série')], max_length=5),
        ),
    ]
