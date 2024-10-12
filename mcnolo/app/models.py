from django.db import models
from django.contrib.auth.models import User
from channels.layers import get_channel_layer
from asgiref.sync import async_to_sync
from mcnolo.settings import MEDIA_URL  # Usamos el modelo de usuario de Django

# Create your models here.
class Producto(models.Model):
    nombre = models.CharField(max_length=100)
    #descripcion = models.TextField(blank=True, null=True)
    descripcion = models.TextField(default="Sin descripción")
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    #disponible = models.BooleanField(default=True)
    imagen = models.ImageField(upload_to='productos/', blank=True, null=True)  # Campo para la imagen
    activo = models.BooleanField(default=True)  # Campo para marcar si está activo o no
    
    def __str__(self):
        return self.nombre
        
        
class Pedido(models.Model):

    ESTADOS = [
        ('en_espera', 'En Espera'),
        ('en_proceso', 'En Proceso'),
        ('finalizado', 'Finalizado'),
        ('rechazado', 'Rechazado'),
        ('listo', 'Listo para enviar'),
        ('enviado', 'Enviado'),
    ]

    usuario = models.ForeignKey(User, on_delete=models.CASCADE)  # Usuario que hace el pedido
    #productos = models.ManyToManyField(Producto, through='ProductoPedido')  # Relación muchos a muchos
    #productos = models.ManyToManyField(Producto)
    fecha = models.DateTimeField(auto_now_add=True)  # Fecha automática del pedido
    total = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    estado = models.CharField(max_length=20, choices=ESTADOS, default="Pendiente")  # Estado del pedido
    
    def save(self, *args, **kwargs):
        # Verificar si el estado cambió a "listo"
        if self.pk is not None:  # Asegurarse de que el pedido ya existe
            previous = Pedido.objects.get(pk=self.pk)
            if previous.estado != self.estado and self.estado == 'listo':
                # Enviar notificación al cliente vía WebSocket
                channel_layer = get_channel_layer()
                async_to_sync(channel_layer.group_send)(
                    f'pedido_{self.id}',
                    {
                        'type': 'pedido_listo',
                        'message': f'Tu pedido {self.id} está listo para recoger.'
                    }
                )
        super().save(*args, **kwargs)

    def __str__(self):
        return f'Pedido {self.id} - {self.usuario.email}'


class ProductoPedido(models.Model):
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    pedido = models.ForeignKey(Pedido, on_delete=models.CASCADE)
    cantidad = models.PositiveIntegerField(default=1)  # Cantidad de productos comprados

    def __str__(self):
        return f'{self.cantidad} x {self.producto.nombre}'

class HistorialProducto(models.Model):
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    accion = models.CharField(max_length=10, choices=[('agregado', 'Agregado'), ('eliminado', 'Eliminado')])
    fecha = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.producto.nombre} - {self.accion} - {self.fecha}'

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    foto = models.ImageField(upload_to='perfil_fotos/', default='perfil_fotos/avatar.webp')

    def __str__(self):
        return f'Perfil de {self.user.username}'
    
class Carrito(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    productos = models.ManyToManyField(Producto, through='CarritoProducto')
    total = models.DecimalField(max_digits=10, decimal_places=2, default=0)

    def calcular_total(self):
        self.total = sum(item.producto.precio * item.cantidad for item in self.carritoproducto_set.all())
        self.save()

class CarritoProducto(models.Model):
    carrito = models.ForeignKey(Carrito, on_delete=models.CASCADE)
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    cantidad = models.IntegerField(default=1)  