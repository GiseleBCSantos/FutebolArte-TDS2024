# Generated by Django 4.2 on 2024-02-28 13:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('localidades', '0003_alter_cidade_options_alter_estado_options_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='estado',
            name='regiao',
            field=models.CharField(default='Não informado', max_length=20, null=True),
        ),
    ]
