# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-08-29 16:32
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('gestion_usuarios', '0001_initial'),
        ('gestion_inventario', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Asignar_recursos',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_joined', models.DateField(auto_now_add=True)),
                ('recursos', models.ManyToManyField(to='gestion_inventario.Recursos')),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gestion_usuarios.Usuario')),
            ],
        ),
    ]
