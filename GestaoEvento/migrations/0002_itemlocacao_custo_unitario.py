# Generated by Django 4.2.1 on 2023-10-11 15:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('GestaoEvento', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='itemlocacao',
            name='custo_unitario',
            field=models.DecimalField(decimal_places=2, default=' ', max_digits=10),
        ),
    ]
