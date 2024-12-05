from django.contrib import admin
from channels.layers import get_channel_layer
from asgiref.sync import async_to_sync
from .models import Producto, Pedido, ProductoPedido, Sugerencia

admin.site.register(Producto)
admin.site.register(ProductoPedido)

# Usa @admin.register para vincular el modelo Pedido con PedidoAdmin
@admin.register(Pedido)
class PedidoAdmin(admin.ModelAdmin):
    list_display = ('usuario', 'invitado_id', 'metodo_pago', 'total', 'estado', 'nota_especial')
    readonly_fields = ('nota_especial',)  # Hacer que la nota especial sea de solo lectura

    actions = [
        'notificar_pedido_listo',
        'aceptar_pedido',
        'rechazar_pedido',
        'poner_en_espera',
        'poner_en_proceso',
        'finalizar_pedido',
        'preparar_recogida',
        'enviar_pedido',
    ]

    def notificar_pedido_listo(self, request, queryset):
        for pedido in queryset:
            pedido.estado = 'listo'
            pedido.save()  # Guardamos el cambio de estado

            # Configuración del WebSocket según sea usuario o invitado
            channel_layer = get_channel_layer()
            if pedido.usuario:  # Usuario autenticado
                group_name = f'pedido_{pedido.id}'
            elif pedido.invitado_id:  # Invitado
                group_name = f'invitado_{pedido.invitado_id}'
            else:
                continue

            # Enviar la notificación al grupo correspondiente
            async_to_sync(channel_layer.group_send)(
                group_name,
                {
                    'type': 'pedido_listo',
                    'message': f'Tu pedido {pedido.id} está listo para ser entregado.'
                }
            )
        self.message_user(request, "Se ha notificado que el pedido está listo.")

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

admin.site.register(Sugerencia)