from django.shortcuts import render, get_object_or_404, redirect
from .models import Producto, Categoria
from django.contrib.auth.decorators import login_required


def home(request):
    productos = Producto.objects.all()  # Obtiene todos los productos
    return render(request, 'productos.html', {'productos': productos})

from django.contrib import messages

def agregar_producto(request):
    if request.method == 'POST':
        nombre = request.POST['nombre']
        descripcion = request.POST['descripcion']
        precio = request.POST['precio']
        cantidad = request.POST['cantidad']
        id_categoria = request.POST['id_categoria']

        try:
            Producto.objects.create(
                nombre=nombre,
                descripcion=descripcion,
                precio=precio,
                cantidad=cantidad,
                id_categoria_id=id_categoria
            )
            messages.success(request, 'Producto agregado con éxito.')
        except Exception as e:
            messages.error(request, f'Error al agregar el producto: {str(e)}')

        return redirect('home')
    else:
        categorias = Categoria.objects.all()
        return render(request, 'agregar_producto.html', {'categorias': categorias})


def editar_producto(request, id_productos):
    producto = get_object_or_404(Producto, id_productos=id_productos)
    if request.method == 'POST':
        producto.nombre = request.POST['nombre']
        producto.descripcion = request.POST['descripcion']
        producto.precio = request.POST['precio']
        producto.cantidad = request.POST['cantidad']
        producto.id_categoria = get_object_or_404(Categoria, id_categoria=request.POST['id_categoria'])
        producto.save()  # Guarda los cambios en la base de datos
        return redirect('home')
    else:
        categorias = Categoria.objects.all()  # Obtener las categorías para el formulario
        return render(request, 'editar_producto.html', {'producto': producto, 'categorias': categorias})
