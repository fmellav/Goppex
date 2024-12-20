# Generated by Django 5.1.4 on 2024-12-14 19:04

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Rol',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_rol', models.CharField(max_length=50, unique=True)),
                ('descripcion', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id_usuario', models.AutoField(primary_key=True, serialize=False)),
                ('nombre_user', models.CharField(max_length=100, unique=True)),
                ('correo', models.EmailField(max_length=254, unique=True)),
                ('password', models.CharField(max_length=128)),
                ('fecha_creacion', models.DateTimeField(auto_now_add=True)),
                ('id_rol', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='login.rol')),
            ],
        ),
    ]
