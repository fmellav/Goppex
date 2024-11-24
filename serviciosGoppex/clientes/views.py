from django.http import JsonResponse
from django.shortcuts import render, redirect, get_object_or_404
from .models import Cliente  # Importar el modelo Cliente
from django.utils import timezone
import csv
from django.http import HttpResponse
from reportlab.pdfgen import canvas

def lista_clientes(request):
    # Obtener todos los clientes desde la base de datos
    clientes = Cliente.objects.all()

    # Pasar los clientes a la pestaña principal
    return render(request, 'clientes/clientes.html', {'clientes': clientes})

def agregar_cliente(request):
    if request.method == 'POST':
        # Recibe los datos del formulario (esto se definirá luego en tu HTML de formulario)
        Cliente.objects.create(
            rut=request.POST['rut'],
            razon_social=request.POST['razon_social'],
            giro=request.POST['giro'],
            direccion=request.POST['direccion'],
            correo=request.POST['correo'],
            telefono=request.POST['telefono'],
        )
        return redirect('clientes')  # Redirige a la lista de clientes
    return render(request, 'clientes/agregar_cliente.html')  # Renderiza el formulario


def ocultar_cliente(request, rut):
    cliente = Cliente.objects.get(rut=rut)
    cliente.fecha_termino = timezone.now()  # Marca la fecha de término como la actual
    cliente.save()
    return redirect('clientes')


def exportar_csv_clientes(request):
    # Crear una respuesta HTTP con contenido CSV
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="clientes.csv"'

    # Crear un escritor CSV
    writer = csv.writer(response)
    writer.writerow(['RUT', 'Razón Social', 'Giro', 'Dirección', 'Correo', 'Teléfono'])

    # Escribir los datos de los clientes en el archivo CSV
    clientes = Cliente.objects.all()
    for cliente in clientes:
        writer.writerow([
            cliente.rut,
            cliente.razon_social,
            cliente.giro,
            cliente.direccion,
            cliente.correo,
            cliente.telefono
        ])

    return response

def exportar_pdf_clientes(request):
    # Crear una respuesta HTTP con contenido PDF
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="clientes.pdf"'

    # Crear un objeto canvas para generar el PDF
    p = canvas.Canvas(response)

    # Título del documento
    p.setFont("Helvetica-Bold", 16)
    p.drawString(200, 800, "Lista de Clientes")

    # Espaciado inicial
    y = 750

    # Escribir los datos de los clientes en el PDF
    clientes = Cliente.objects.all()
    p.setFont("Helvetica", 12)

    for cliente in clientes:
        texto = f"{cliente.rut} - {cliente.razon_social} - {cliente.giro} - {cliente.correo}"
        p.drawString(50, y, texto)
        y -= 20
        if y < 50:  # Salto de página si el contenido sobrepasa el límite
            p.showPage()
            p.setFont("Helvetica", 12)
            y = 800

    # Finalizar el PDF
    p.showPage()
    p.save()

    return response

def ver_clientes_ocultos(request):
    # Filtrar clientes que tienen una fecha de término (ocultos)
    clientes_ocultos = Cliente.objects.filter(fecha_termino__isnull=False)
    return render(request, 'clientes/clientes_ocultos.html', {'clientes': clientes_ocultos})

def editar_cliente(request, rut):
    cliente = get_object_or_404(Cliente, rut=rut)

    if request.method == 'POST':
        # Actualizar los datos del cliente con la información del formulario
        cliente.razon_social = request.POST['razon_social']
        cliente.giro = request.POST['giro']
        cliente.direccion = request.POST['direccion']
        cliente.correo = request.POST['correo']
        cliente.telefono = request.POST['telefono']
        cliente.save()  # Guardar los cambios
        return redirect('clientes')  # Redirigir a la lista de clientes

    # Si es un GET, mostrar el formulario con los datos actuales
    return render(request, 'clientes/editar_cliente.html', {'cliente': cliente})