# Generated by Django 4.2 on 2024-02-28 13:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Times', '0004_alter_competicao_options_alter_jogador_options_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='competicao',
            options={},
        ),
        migrations.AlterModelOptions(
            name='jogador',
            options={'verbose_name_plural': 'Jogadores'},
        ),
        migrations.AlterModelOptions(
            name='time',
            options={},
        ),
        migrations.AlterModelOptions(
            name='titulo',
            options={},
        ),
        migrations.RemoveField(
            model_name='time',
            name='titulos',
        ),
        migrations.AlterField(
            model_name='time',
            name='divisao_atual',
            field=models.CharField(max_length=5),
        ),
        migrations.AlterField(
            model_name='titulo',
            name='colocacao',
            field=models.CharField(choices=[('1°', '1° Lugar'), ('2°', '2° Lugar'), ('3°', '3° Lugar')], max_length=10),
        ),
    ]
