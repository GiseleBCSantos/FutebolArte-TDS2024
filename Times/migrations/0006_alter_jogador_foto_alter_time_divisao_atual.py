# Generated by Django 4.2 on 2024-02-28 13:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Times', '0005_alter_competicao_options_alter_jogador_options_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='jogador',
            name='foto',
            field=models.ImageField(blank=True, upload_to='Times/Jogadores'),
        ),
        migrations.AlterField(
            model_name='time',
            name='divisao_atual',
            field=models.CharField(choices=[('A', 'Série A'), ('B', 'Série B'), ('C', 'Série C'), ('D', 'Série D'), ('S', 'Sem série')], max_length=5),
        ),
    ]
