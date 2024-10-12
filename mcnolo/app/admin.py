from django.contrib import admin
from channels.layers import get_channel_layer
from asgiref.sync import async_to_sync
from .models import Producto, Pedido, ProductoPedido

admin.site.register(Producto)
admin.site.register(ProductoPedido)

# Usa @admin.register para vincular el modelo Pedido con PedidoAdmin
@admin.register(Pedido)
class PedidoAdmin(admin.ModelAdmin):
    list_display = ('usuario', 'total', 'estado')

    actions = ['notificar_pedido_listo']  # Añade la acción en la lista de acciones

    def notificar_pedido_listo(self, request, queryset):
        for pedido in queryset:
            pedido.estado = 'listo'  # Cambiar el estado del pedido a "listo"
            pedido.save()

            # Notificar al cliente vía WebSocket
            channel_layer = get_channel_layer()
            async_to_sync(channel_layer.group_send)(
                f'pedido_{pedido.id}',
                {
                    'type': 'pedido_listo',
                    'message': f'Tu pedido {pedido.id} está listo para ser entregado.'
                }
            )
        self.message_user(request, "El cliente ha sido notificado de que el pedido está listo.")

    notificar_pedido_listo.short_description = "Notificar que el pedido está listo"
