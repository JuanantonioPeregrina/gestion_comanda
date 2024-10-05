from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages
from .models import Producto

# Página principal
def index(request):
    return render(request, 'app/index.html')

# Vista de inicio de sesión
def inicio_sesion(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        
        # Autenticar el usuario con el email y contraseña
        user = authenticate(request, username=email, password=password)
        
        if user is not None:
            login(request, user)
            return redirect('pagina_principal')
        else:
            messages.error(request, 'Correo o contraseña incorrectos')

    return render(request, 'app/InicioSesion.html')

# Página mostrada cuando el usuario ha iniciado sesión
# Página mostrada cuando el usuario ha iniciado sesión
def pagina_principal(request):
    productos = Producto.objects.filter(disponible=True)  # Solo muestra los productos disponibles
    return render(request, 'app/PaginaPrincipal.html', {'productos': productos})

