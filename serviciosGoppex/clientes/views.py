from django.http import JsonResponse
from django.shortcuts import render, redirect, get_object_or_404
from .models import Cliente  # Importar el modelo Cliente
from django.utils import timezone
import csv
from django.http import HttpResponse
from reportlab.pdfgen import canvas
from django.db import connection
from django.shortcuts import render, redirect

def lista_clientes(request):
    # Obtener todos los clientes desde la base de datos
    clientes = Cliente.objects.all()

    # Pasar los clientes a la pestaña principal
    return render(request, 'clientes/clientes.html', {'clientes': clientes})

def agregar_cliente(request):
    if request.method == 'POST':  # Verifica si la solicitud es de tipo POST (envío del formulario)
        # Recoge los datos enviados desde el formulario
        rut = request.POST['rut']
        razon_social = request.POST['razon_social']
        giro = request.POST['giro']
        direccion = request.POST['direccion']
        correo = request.POST['correo']
        telefono = request.POST['telefono']
        
        # Llamar al procedimiento almacenado 'AgregarCliente' para insertar el cliente en la base de datos
        with connection.cursor() as cursor:  # Abre un cursor para ejecutar comandos SQL directamente
            cursor.callproc('AgregarCliente', [rut, razon_social, giro, direccion, correo, telefono])  
            # Llama al procedimiento almacenado con los parámetros correspondientes
        
        return redirect('clientes')  # Redirige al usuario a la lista de clientes después de agregar uno nuevo

    return render(request, 'clientes/agregar_cliente.html')  
    # Si la solicitud no es POST (por ejemplo, GET), renderiza la página del formulario de agregar cliente


def ocultar_cliente(request, rut):
    # Recuperar el cliente con el RUT específico
    cliente = Cliente.objects.get(rut=rut)  # Busca el cliente en la base de datos utilizando el RUT

    # Marcar el cliente como "oculto" asignando la fecha de término actual
    cliente.fecha_termino = timezone.now()  # Asigna la fecha actual al campo 'fecha_termino'
    cliente.save()  # Guarda los cambios en la base de datos

    return redirect('clientes')  # Redirige al usuario a la lista de clientes después de ocultar uno



def exportar_csv_clientes(request):
    # Crear una respuesta HTTP con contenido CSV
    response = HttpResponse(content_type='text/csv')  # Define el tipo de contenido como CSV
    response['Content-Disposition'] = 'attachment; filename="clientes.csv"'  # Indica al navegador que descargue el archivo con este nombre

    # Crear un escritor CSV
    writer = csv.writer(response)  # Inicializa un escritor CSV usando la respuesta como destino
    writer.writerow(['RUT', 'Razón Social', 'Giro', 'Dirección', 'Correo', 'Teléfono'])  # Escribe la fila de encabezado en el archivo CSV

    # Escribir los datos de los clientes en el archivo CSV
    clientes = Cliente.objects.all()  # Obtiene todos los objetos de la tabla "Cliente"
    for cliente in clientes:  # Itera sobre cada cliente en la base de datos
        writer.writerow([  # Escribe una fila en el archivo CSV con los datos del cliente
            cliente.rut,
            cliente.razon_social,
            cliente.giro,
            cliente.direccion,
            cliente.correo,
            cliente.telefono
        ])

    return response  # Devuelve la respuesta con el archivo CSV adjunto

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