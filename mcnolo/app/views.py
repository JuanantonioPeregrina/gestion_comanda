import json
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login
from django.contrib import messages
from .models import HistorialProducto, Pedido, Producto, Carrito, CarritoProducto, ProductoPedido, Oferta
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from channels.layers import get_channel_layer
from asgiref.sync import async_to_sync
from django.http import JsonResponse
from django.core.mail import send_mail
from .forms import ChangeUsernameForm



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
#@login_required  # Esto asegura que solo los usuarios autenticados puedan acceder

def pagina_principal(request):
    # Mostrar solo productos activos para todos los usuarios
    productos = Producto.objects.filter(activo=True)

    # Comprobar si el usuario es autenticado o si es invitado
    es_invitado = request.session.get('es_invitado', False)

    if request.user.is_authenticated:
        # Si el usuario es autenticado
        if request.user.is_staff:
            productos = Producto.objects.all()  # Mostrar todos los productos si es staff

        # Obtener los pedidos del usuario autenticado
        pedidos = Pedido.objects.filter(usuario=request.user) 
        pedido = pedidos.last() if pedidos else None  # Último pedido para la notificación
        return render(request, 'app/PaginaPrincipal.html', {
            'productos': productos,
            'pedidos': pedidos,  # Lista de pedidos para historial
            'pedido': pedido,  # Último pedido
            'invitado': False  # Indicar que no es invitado
        })

    # Si el usuario es invitado (no autenticado)
    elif es_invitado:
        return render(request, 'app/PaginaPrincipal.html', {
            'productos': productos,
            'invitado': True  # Indicar que es invitado
        })
    
    # Si el usuario no está autenticado ni es invitado, redirigir al inicio de sesión
    return redirect('inicio_sesion')



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
                crear_usuario_oferta(email, password)
                messages.success(request, 'Registro exitoso. Ahora puedes iniciar sesión.')
                # Asegúrate de que 'inicio_sesion' esté definida en tu urls.py
                return redirect('inicio_sesion')
        else:
            messages.error(request, 'Las contraseñas no coinciden.')

    return render(request, 'app/registro.html')
def crear_usuario_oferta(email, password):
    user = User.objects.create_user(username=email, email=email, password=password)
    user.save()
    Oferta.objects.create(usuario=user, descuento=10, codigo=f'{user.username}_10')
    enviar_correo(email,user,f'{user.username}_10')
    

def enviar_correo(mail, user, oferta):
    send_mail(
        'Oferta de bienvenida',
        f'¡Hola {user.username}! Te hemos dado una oferta del 10%. Usa el código: {oferta}',
        'no-reply@tuapp.com',
        [mail],
        fail_silently=False,
    )

def anadir_plato(request):
    if request.method == 'POST':
        nombre_plato = request.POST.get('nombre_plato')
        descripcion = request.POST.get('descripcion')
        precio =   request.POST.get('precio')
        tiempo_preparacion = request.POST.get('tiempo_preparacion')
        #disponible = 'disponible' in request.POST
        activo = 'disponible' in request.POST
        #disponible = request.POST.get('disponible')
        imagen = request.FILES.get('imagen')

        nuevo_plato = Producto(nombre=nombre_plato, descripcion=descripcion, precio=precio, tiempo_preparacion=tiempo_preparacion, activo=activo, imagen=imagen)
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
    # Si es una solicitud POST, se está intentando finalizar la compra
    if request.method == 'POST':
        # Leer el cuerpo de la solicitud que llega en formato JSON
        data = json.loads(request.body)
        cart = data.get('cart', [])
        total = data.get('total', 0)
        # nota_especial = data.get('nota_especial', '')  # Obtener la nota especial
        nota_especial = json.loads(request.body).get('nota_especial')
        # nota_especial = request.POST.get('nota_especial')  # Captura la nota especial
        # Verificar que el carrito no esté vacío
        if not cart:
            return JsonResponse({'error': 'El carrito está vacío.'}, status=400)

        # Crear el pedido y almacenar en la base de datos
        pedido = Pedido.objects.create(usuario=request.user, total=total, nota_especial=nota_especial)

        # Inicializar tiempo total de preparación
        tiempo_total_preparacion = 0

        # Guardar cada producto en el pedido y calcular el tiempo de preparación
        for item in cart:
            producto = Producto.objects.get(nombre=item['name'])
            ProductoPedido.objects.create(pedido=pedido, producto=producto, cantidad=1)
            tiempo_total_preparacion += producto.tiempo_preparacion  # Sumar el tiempo de preparación

        # Devolver el total y el tiempo estimado de preparación
        return JsonResponse({
            'total': total,
            'tiempo_estimado': tiempo_total_preparacion  # Enviar el tiempo total de preparación
        })
    
    # Si es una solicitud GET, mostrar los detalles del carrito en formato JSON
    elif request.method == 'GET':
        carrito = Carrito.objects.get(usuario=request.user)  # Obtén el carrito del usuario
        productos = carrito.productos.all()

        # Calcular el tiempo total de preparación
        tiempo_total_preparacion = sum(producto.tiempo_preparacion for producto in productos)

        # Devolver los detalles del carrito en JSON
        return JsonResponse({
            'productos': [
                {'nombre': producto.nombre, 'precio': producto.precio, 'tiempo_preparacion': producto.tiempo_preparacion, 'nota_especial': pedido.nota_especial}
                for producto in productos
            ],
            'tiempo_total_preparacion': tiempo_total_preparacion,
        })

    # Si el método no es ni POST ni GET, devuelve un error
    return JsonResponse({'error': 'Método no permitido.'}, status=405)


def obtener_estado_pedido(request, pedido_id):
    pedido = Pedido.objects.get(id=pedido_id, usuario=request.user)  # Asegúrate de que el pedido pertenece al usuario autenticado
    return JsonResponse({'estado': pedido.get_estado_display()})  # Devuelve el estado legible del pedido

def comprobar_oferta(request):
    data = json.loads(request.body)
    codigo = data.get('codigo')  # Obtener el código enviado desde el formulario
    # Buscar la oferta en la base de datos
    oferta = Oferta.objects.filter(codigo=codigo).first()

    if oferta:
        # Si se encuentra una oferta válida, calcular el descuento
        oferta_aplicable = 1 - (oferta.descuento / 100)
        return JsonResponse({'oferta_aplicable': oferta_aplicable})
    else:
        # Si el código de la oferta no es válido
        return JsonResponse({'error': 'Código de oferta no válido'}, status=400)

@login_required   
def change_username(request):
    if request.method == 'POST':
        new_username = request.POST.get('username')
        if new_username:
            request.user.username = new_username
            request.user.save()
            messages.success(request, 'Nombre de usuario cambiado con éxito')
            return redirect('pagina_principal')  # Redirigir después de cambiar
        else:
            messages.error(request, 'Por favor, introduce un nombre de usuario válido')
    return render(request, 'app/change_username.html', {'user': request.user})

@login_required
def change_image(request):
    if request.method == 'POST':
        profile = request.user.profile  
        image = request.FILES.get('image')
        if image:
            profile.foto = image  # 'foto' es el campo de imagen en el modelo Profile
            profile.save()
            messages.success(request, 'Imagen de perfil actualizada con éxito')
            return redirect('pagina_principal')
        else:
            messages.error(request, 'Por favor, selecciona una imagen válida')
    return render(request, 'app/change_image.html')


def finalizar_compra(request):
    # Si es una solicitud POST, se está intentando finalizar la compra
    if request.method == 'POST':
        # Leer el cuerpo de la solicitud que llega en formato JSON
        data = json.loads(request.body)
        nombre_producto = data.get('nombre')  # Obtener el nombre del producto
        precio_producto = data.get('precio', 0)  # Obtener el precio del producto, default 0
        nota_especial = data.get('nota_especial', '')  # Obtener la nota especial, por defecto ''

        # Verificar que se haya proporcionado un nombre de producto
        if not nombre_producto:
            return JsonResponse({'error': 'El nombre del producto es obligatorio.'}, status=400)

        # Verificar que se haya proporcionado un precio del producto
        if precio_producto <= 0:
            return JsonResponse({'error': 'El precio del producto debe ser mayor que cero.'}, status=400)

        # Crear el pedido y almacenar en la base de datos
        producto = Producto.objects.get(nombre=nombre_producto)  # Buscar el producto por su nombre
        pedido = Pedido.objects.create(usuario=request.user, total=precio_producto, nota_especial=nota_especial)

        # Crear el registro del producto en el pedido
        ProductoPedido.objects.create(pedido=pedido, producto=producto, cantidad=1)

        # Devolver el total y el tiempo estimado de preparación
        return JsonResponse({
            'total': precio_producto,
            'tiempo_estimado': producto.tiempo_preparacion  # Enviar el tiempo de preparación del producto
        })

    # Si el método no es POST, devuelve un error
    return JsonResponse({'error': 'Método no permitido.'}, status=405)

def invitado(request):
     # Configura una variable en la sesión para identificar que es un "invitado"
    request.session['es_invitado'] = True
    return redirect('pagina_principal')  # Redirige a la página principal
