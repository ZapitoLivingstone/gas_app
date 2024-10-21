# Generated by Django 5.1.1 on 2024-10-21 15:20

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('solicitudes', '0002_delete_solicitud'),
    ]

    operations = [
        migrations.CreateModel(
            name='Solicitud',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rut', models.CharField(max_length=12)),
                ('nombre', models.CharField(max_length=100)),
                ('apellido', models.CharField(max_length=100)),
                ('direccion', models.CharField(max_length=255)),
                ('telefono', models.CharField(max_length=15)),
                ('comuna', models.CharField(max_length=100)),
                ('fecha_solicitud', models.DateTimeField(auto_now_add=True)),
                ('fecha_aceptacion', models.DateTimeField(blank=True, null=True)),
                ('estado', models.CharField(choices=[('P', 'PENDIENTE'), ('A', 'ACEPTADA'), ('R', 'RECHAZADA'), ('E', 'EXPIRADA')], default='P', max_length=1)),
            ],
        ),
    ]