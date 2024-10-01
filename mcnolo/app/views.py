from django.shortcuts import render # type: ignore

def index(request):
    return render(request, 'app/index.html')

def inicio_sesion(request):
    return render(request, 'app/inicioSesion.html')

def pagina_principal(request):
    return render(request, 'app/paginaPrincipal.html')