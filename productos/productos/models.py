from django.db import models

class Categoria(models.Model):
    id_categoria = models.AutoField(primary_key=True)  # ID único de la categoría
    nombre = models.CharField(max_length=100, unique=True)  # Nombre de la categoría, único

    def __str__(self):
        return self.nombre

class Producto(models.Model):
    id_productos = models.AutoField(primary_key=True)  # ID único del producto
    nombre = models.CharField(max_length=100)  # Nombre del producto
    descripcion = models.TextField()  # Descripción del producto
    precio = models.DecimalField(max_digits=10, decimal_places=2)  # Precio general
    cantidad = models.PositiveIntegerField()  # Stock actual
    id_categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)  # Relación con la categoría

    def __str__(self):
        return self.nombre
