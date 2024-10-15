from django.contrib import admin
from channels.layers import get_channel_layer
from asgiref.sync import async_to_sync
from .models import Producto, Pedido, ProductoPedido

admin.site.register(Producto)
admin.site.register(ProductoPedido)

# Usa @admin.register para vincular el modelo Pedido con PedidoAdmin
@admin.register(Pedido)
class PedidoAdmin(admin.ModelAdmin):
    list_display = ('usuario', 'total', 'nota_especial', 'estado')
    readonly_fields = ('nota_especial',)  # Hacer que la nota especial sea de solo lectura

    actions = ['notificar_pedido_listo'
                'aceptar_pedido',
                'rechazar_pedido',
                'poner_en_espera',
                'poner_en_proceso',
                'finalizar_pedido',
                'preparar_recogida',
                'enviar_pedido'
    ]
     # Añade la acción en la lista de acciones

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
 # Acción para aceptar el pedido
    def aceptar_pedido(self, request, queryset):
        for pedido in queryset:
            pedido.estado = 'aceptado'
            pedido.save()
            self.message_user(request, "El pedido ha sido aceptado.")

    # Acción para rechazar el pedido
    def rechazar_pedido(self, request, queryset):
        for pedido in queryset:
            pedido.estado = 'rechazado'
            pedido.save()
            self.message_user(request, "El pedido ha sido rechazado.")

    # Poner en espera
    def poner_en_espera(self, request, queryset):
        for pedido in queryset:
            pedido.estado = 'en_espera'
            pedido.save()
            self.message_user(request, "El pedido está en espera.")

    # Poner en proceso
    def poner_en_proceso(self, request, queryset):
        for pedido in queryset:
            pedido.estado = 'en_proceso'
            pedido.save()
            self.message_user(request, "El pedido está en proceso.")

    # Finalizar pedido
    def finalizar_pedido(self, request, queryset):
        for pedido in queryset:
            pedido.estado = 'finalizado'
            pedido.save()
            self.message_user(request, "El pedido ha sido finalizado.")

    # Preparar para recoger
    def preparar_recogida(self, request, queryset):
        for pedido in queryset:
            pedido.estado = 'recoger'
            pedido.save()
            self.message_user(request, "El pedido está listo para ser recogido.")

    # Enviar pedido
    def enviar_pedido(self, request, queryset):
        for pedido in queryset:
            pedido.estado = 'enviado'
            pedido.save()
            self.message_user(request, "El pedido ha sido enviado.")