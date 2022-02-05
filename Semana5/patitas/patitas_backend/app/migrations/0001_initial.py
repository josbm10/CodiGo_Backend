# Generated by Django 4.0.1 on 2022-01-31 22:59

import cloudinary.models
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Mascotas',
            fields=[
                ('mascota_id', models.AutoField(primary_key=True, serialize=False)),
                ('mascota_nom', models.CharField(max_length=100, verbose_name='Nombre')),
                ('mascota_est', models.CharField(choices=[('DISPONIBLE', 'DISPONIBLE'), ('NO DISPONIBLE', 'NO DISPONIBLE')], max_length=20, verbose_name='Estado')),
                ('mascota_img', cloudinary.models.CloudinaryField(default='', max_length=255, verbose_name='Imagen')),
                ('mascota_age', models.IntegerField(default=0, verbose_name='Edad')),
                ('mascota_sex', models.CharField(choices=[('HEMBRA', 'HEMBRA'), ('MACHO', 'MACHO')], max_length=10, verbose_name='Sexo')),
                ('mascota_act', models.CharField(choices=[('ALTO', 'ALTO'), ('MEDIO', 'MEDIO'), ('BAJO', 'BAJO')], max_length=10, verbose_name='Nivel de Actividad')),
                ('mascota_hair', models.CharField(choices=[('CORTO', 'CORTO'), ('LARGO', 'LARGO')], max_length=10, verbose_name='Pelo')),
                ('mascota_tall', models.CharField(choices=[('PEQUEÑO', 'PEQUEÑO'), ('MEDIANO', 'MEDIANO'), ('GRANDE', 'GRANDE')], max_length=10, verbose_name='Tamaño')),
                ('mascota_hty', models.TextField()),
            ],
        ),
    ]