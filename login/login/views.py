from django.shortcuts import render, redirect
from django.contrib.auth import logout
from django.contrib import messages
from .models import Usuario
from django.contrib.auth.hashers import check_password

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        try:
            # Busca al usuario en la base de datos
            user = Usuario.objects.get(nombre_user=username)

            # Valida la contraseña
            if check_password(password, user.password):
                # Redirigir según el rol
                if user.id_rol.nombre_rol == 'cliente':
                    return redirect('http://127.0.0.1:8002/')  # Servicio de clientes
                elif user.id_rol.nombre_rol == 'producto':
                    return redirect('http://127.0.0.1:8003/')  # Servicio de productos

                else:
                    messages.error(request, 'No tienes permisos para acceder.')
                    return redirect('login')

            else:
                messages.error(request, 'Usuario o Contraseña incorrecta.')

        except Usuario.DoesNotExist:
            messages.error(request, 'Usuario o Contraseña incorrecta.')

        except Exception as e:
            # Captura cualquier otro error inesperado
            messages.error(request, f'Ocurrió un error inesperado: {str(e)}')

        return redirect('login')

    return render(request, 'login.html')


def logout_view(request):
    """
    Cierra la sesión del usuario y lo redirige al login.
    """
    logout(request)  # Cierra la sesión
    return redirect('login')  # Redirige al login
