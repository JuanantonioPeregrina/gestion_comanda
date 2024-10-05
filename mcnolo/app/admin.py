from django.contrib import admin

from .models import Producto, Pedido, ProductoPedido

admin.site.register(Producto)
admin.site.register(Pedido)
admin.site.register(ProductoPedido)
# Register your models here.
