from django.db import models

class Cliente(models.Model):
    rut = models.CharField(max_length=12, primary_key=True)  # Clave primaria Identificador único del cliente (ej: 12.345.678-9)
    razon_social = models.CharField(max_length=150)  # Nombre comercial
    giro = models.CharField(max_length=100)  # Actividad económica del cliente
    direccion = models.TextField()  # Dirección del cliente
    correo = models.EmailField(unique=True)  # Correo del cliente
    telefono = models.CharField(max_length=15)  # Teléfono de contacto
    fecha_inicio = models.DateField(auto_now_add=True)  # Fecha de registro automática
    fecha_termino = models.DateField(null=True, blank=True)  # Fecha de baja (opcional)

    def __str__(self):
        return self.razon_social
