from django.shortcuts import render

from django.http import JsonResponse

def prueba_inventario(request):
    # Respuesta de prueba
    return JsonResponse({'mensaje': 'Prueba de inventario exitosa'})

