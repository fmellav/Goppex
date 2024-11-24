from django.urls import path
from . import views

urlpatterns = [
    path('', views.lista_clientes, name='clientes'),  # Página principal de clientes
    path('agregar/', views.agregar_cliente, name='agregar_cliente'),  # Agregar cliente
    path('editar/<str:rut>/', views.editar_cliente, name='editar_cliente'),  # Editar cliente
    path('exportar/csv/', views.exportar_csv_clientes, name='exportar_csv_clientes'),  # Exportar CSV
    path('exportar/pdf/', views.exportar_pdf_clientes, name='exportar_pdf_clientes'),  # Exportar PDF
    path('ver_ocultos/', views.ver_clientes_ocultos, name='ver_clientes_ocultos'),  # Ver clientes ocultos
    path('ocultar/<str:rut>/', views.ocultar_cliente, name='ocultar_cliente'),  # Ocultar cliente
]
