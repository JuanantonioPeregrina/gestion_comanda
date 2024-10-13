import json
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login
from django.contrib import messages
from .models import HistorialProducto, Pedido, Producto, Carrito, CarritoProducto, ProductoPedido
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from channels.layers import get_channel_layer
from asgiref.sync import async_to_sync
from django.http import JsonResponse


# Página principal
def index(request):
    return render(request, 'app/index.html')

# Vista de inicio de sesión
def inicio_sesion(request):
    # Verificar si el usuario ya está autenticado
    if request.user.is_authenticated:
        return redirect('pagina_principal')  # Redirigir directamente a la página principal si ya ha iniciado sesión

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
@login_required  # Esto asegura que solo los usuarios autenticados puedan acceder
#def pagina_principal(request):
    #productos = Producto.objects.all()  # Solo muestra los productos disponibles
    #productos = Producto.objects.filter(activo=True)  # Solo productos activos
    #return render(request, 'app/PaginaPrincipal.html', {'productos': productos})*/


def pagina_principal(request):
    if request.user.is_staff:
        # Si es administrador, mostrar todos los productos, tanto activos como inactivos
        productos = Producto.objects.all()
    else:
        # Si es un usuario normal, mostrar solo los productos activos
        productos = Producto.objects.filter(activo=True)

    # Obtener todos los pedidos del usuario (para el historial) y el último pedido (para la notificación)
    pedidos = Pedido.objects.filter(usuario=request.user) if request.user.is_authenticated else None
    pedido = pedidos.last() if pedidos else None  # Último pedido para la notificación

    return render(request, 'app/PaginaPrincipal.html', {
        'productos': productos,
        'pedidos': pedidos,  # Lista completa de pedidos para el historial
        'pedido': pedido  # Último pedido para la notificación
    })


def registrarse(request):
    if request.method == 'POST':
        nombre_completo = request.POST.get('nombre_completo')
        email = request.POST.get('email')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')

        if password == confirm_password:
            # Comprobar si el email ya está en uso
            if User.objects.filter(email=email).exists():
                messages.error(request, 'El correo electrónico ya está registrado.')
            else:
                # Crear el usuario
                user = User.objects.create_user(username=email, email=email, password=password)
                user.save()
                messages.success(request, 'Registro exitoso. Ahora puedes iniciar sesión.')
                return redirect('inicio_sesion')  # Asegúrate de que 'inicio_sesion' esté definida en tu urls.py
        else:
            messages.error(request, 'Las contraseñas no coinciden.')

    return render(request, 'app/registro.html')

def anadir_plato(request):
    if request.method == 'POST':
        nombre_plato = request.POST.get('nombre_plato')
        descripcion = request.POST.get('descripcion')
        precio =   request.POST.get('precio')
        disponible = 'disponible' in request.POST
        #disponible = request.POST.get('disponible')
        imagen = request.FILES.get('imagen')

        nuevo_plato = Producto(nombre=nombre_plato, descripcion=descripcion, precio=precio, disponible=disponible, imagen=imagen)
        nuevo_plato.save()
        return redirect('pagina_principal')
    
def eliminar_producto(request, producto_id):
    producto = get_object_or_404(Producto, id=producto_id)
    producto.activo = False  # Marcar como inactivo en lugar de eliminar
    producto.save()
    HistorialProducto.objects.create(producto=producto, accion='eliminado')
    return redirect('pagina_principal')  # Redirige a la página principal después de eliminar

def restaurar_producto(request, producto_id):
    producto = get_object_or_404(Producto, id=producto_id)
    producto.activo = True  # Volver a activar el producto
    producto.save()
    return redirect('pagina_principal')

def cambiar_visibilidad_producto(request, producto_id):
    producto = Producto.objects.get(id=producto_id)
    producto.activo = not producto.activo  # Cambiar visibilidad
    producto.save()
    return redirect('pagina_principal')


def pedido_listo(request, pedido_id):
    # Lógica para marcar el pedido como listo
    pedido = get_object_or_404(Pedido, id=pedido_id)
    pedido.estado = 'listo'
    pedido.save()

    # Notificar al cliente vía WebSocket
    channel_layer = get_channel_layer()
    async_to_sync(channel_layer.group_send)(
        f'pedido_{pedido_id}',
        {
            'type': 'pedido_listo',
            'message': 'Tu pedido está listo para recoger.'
        }
    )

    return redirect('admin:index')  # Redirigir a donde prefieras en el admin

def anadir_al_carrito(request, producto_id):
    carrito = request.session.get('carrito', [])
    if producto_id not in carrito:
        carrito.append(producto_id)
    request.session['carrito'] = carrito
    messages.success(request, "Producto añadido al carrito.")
    return redirect('pagina_principal')

def agregar_al_carrito(request, producto_id):
    producto = get_object_or_404(Producto, id=producto_id)
    carrito, created = Carrito.objects.get_or_create(usuario=request.user)
    carrito_producto, created = CarritoProducto.objects.get_or_create(carrito=carrito, producto=producto)
    carrito_producto.cantidad += 1
    carrito_producto.save()
    carrito.calcular_total()
    return JsonResponse({'status': 'success', 'total': carrito.total})


def finalizar_compra(request):
    if request.method == 'POST':
        # Leer el cuerpo de la solicitud que llega en formato JSON
        data = json.loads(request.body)
        cart = data.get('cart', [])
        total = data.get('total', 0)

        # Verificar que el carrito no esté vacío
        if not cart:
            return JsonResponse({'error': 'El carrito está vacío.'}, status=400)

        # Crear el pedido y almacenar en la base de datos
        pedido = Pedido.objects.create(usuario=request.user, total=total)

        # Guardar cada producto en el pedido
        for item in cart:
            producto = Producto.objects.get(nombre=item['name'])
            ProductoPedido.objects.create(pedido=pedido, producto=producto, cantidad=1)

        # Redirigir a la página principal después de finalizar la compra
        return JsonResponse({'total': total})
    
    return JsonResponse({'error': 'Método no permitido.'}, status=405)



def obtener_estado_pedido(request, pedido_id):
    pedido = Pedido.objects.get(id=pedido_id, usuario=request.user)  # Asegúrate de que el pedido pertenece al usuario autenticado
    return JsonResponse({'estado': pedido.get_estado_display()})  # Devuelve el estado legible del pedido
