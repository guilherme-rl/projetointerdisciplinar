# Generated by Django 4.2.1 on 2023-11-20 23:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('GestaoEvento', '0004_unidademedida_excluido'),
    ]

    operations = [
        migrations.RenameField(
            model_name='ingrediente',
            old_name='custo_unidade',
            new_name='custo_unitario',
        ),
    ]
