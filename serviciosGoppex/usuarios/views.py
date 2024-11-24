from django.shortcuts import render

from django.http import JsonResponse

def prueba_usuarios(request):
    # Respuesta de prueba
    return JsonResponse({'mensaje': 'Prueba de usuarios exitosa'})
