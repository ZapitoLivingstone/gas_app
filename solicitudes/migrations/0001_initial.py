# Generated by Django 5.1.1 on 2024-10-19 17:33

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Solicitud',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rut', models.CharField(max_length=12, unique=True)),
                ('nombre', models.CharField(max_length=255)),
                ('apellido', models.CharField(max_length=255)),
                ('direccion', models.CharField(max_length=255)),
                ('telefono', models.CharField(max_length=15)),
                ('comuna', models.CharField(max_length=100)),
                ('fecha_solicitud', models.DateTimeField(default=django.utils.timezone.now)),
                ('fecha_aceptacion', models.DateTimeField(blank=True, null=True)),
                ('estado', models.CharField(choices=[('PENDIENTE', 'Pendiente'), ('ACEPTADA', 'Aceptada'), ('RECHAZADA', 'Rechazada'), ('EXPIRADA', 'Expirada')], default='PENDIENTE', max_length=10)),
            ],
        ),
    ]