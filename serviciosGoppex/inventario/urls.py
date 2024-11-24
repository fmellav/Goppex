from django.urls import path
from . import views

urlpatterns = [
    # Aquí defines las rutas específicas de 'inventario'
    # Ejemplo:
    path('prueba/', views.prueba_inventario, name='prueba_inventario'),
]
