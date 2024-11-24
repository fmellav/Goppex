from django.db import models

class Rol(models.Model):
    nombre_rol = models.CharField(max_length=50, unique=True)  # Nombre del rol
    descripcion = models.TextField()  # Descripción del rol

    def __str__(self):
        return self.nombre_rol

class Usuario(models.Model):
    id_usuario = models.AutoField(primary_key=True)  # ID único generado automáticamente
    nombre_user = models.CharField(max_length=100)  # Nombre del usuario
    correo = models.EmailField(unique=True)  # Correo del usuario
    password = models.CharField(max_length=128)  # Contraseña en formato hash
    fecha_creacion = models.DateTimeField(auto_now_add=True)  # Fecha de creación
    id_rol = models.ForeignKey(Rol, on_delete=models.CASCADE)  # Relación con la tabla Rol

    def __str__(self):
        return self.nombre_user
