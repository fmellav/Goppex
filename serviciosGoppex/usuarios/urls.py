from django.urls import path
from . import views  # Importa las vistas de la app 'usuarios'

urlpatterns = [
    path('prueba/', views.prueba_usuarios, name='prueba_usuarios'),  # Ruta para la vista 'prueba_usuarios'
]
