# Generated by Django 5.1.4 on 2024-12-14 13:48

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('id_categoria', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=100, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Producto',
            fields=[
                ('id_productos', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=100)),
                ('descripcion', models.TextField()),
                ('precio', models.DecimalField(decimal_places=2, max_digits=10)),
                ('cantidad', models.PositiveIntegerField()),
                ('id_categoria', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='productos.categoria')),
            ],
        ),
    ]
