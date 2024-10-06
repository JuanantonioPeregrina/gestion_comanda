from django.db import models
from django.contrib.auth.models import User  # Usamos el modelo de usuario de Django

# Create your models here.
class Producto(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField(blank=True, null=True)
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    disponible = models.BooleanField(default=True)
    imagen = models.ImageField(upload_to='productos/', blank=True, null=True)  # Campo para la imagen
    
    def __str__(self):
        return self.nombre
        
        

class Pedido(models.Model):
    cliente = models.ForeignKey(User, on_delete=models.CASCADE)  # Usuario que hace el pedido
    productos = models.ManyToManyField(Producto, through='ProductoPedido')  # Relación muchos a muchos
    fecha_pedido = models.DateTimeField(auto_now_add=True)  # Fecha automática del pedido
    total = models.DecimalField(max_digits=10, decimal_places=2)  # Precio total del pedido

    def __str__(self):
        return f'Pedido #{self.id} de {self.cliente}'


class ProductoPedido(models.Model):
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    pedido = models.ForeignKey(Pedido, on_delete=models.CASCADE)
    cantidad = models.PositiveIntegerField(default=1)  # Cantidad de productos comprados

    def __str__(self):
        return f'{self.cantidad} x {self.producto.nombre}'
