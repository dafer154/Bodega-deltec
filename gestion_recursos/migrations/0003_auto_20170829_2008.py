# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-08-29 20:08
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('gestion_recursos', '0002_asignar_recurso'),
    ]

    operations = [
        migrations.AlterField(
            model_name='asignar_recurso',
            name='recursos',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gestion_inventario.Recursos', unique=True),
        ),
    ]