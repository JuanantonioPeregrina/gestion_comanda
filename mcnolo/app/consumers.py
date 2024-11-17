from channels.generic.websocket import AsyncWebsocketConsumer
import json

class PedidoConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        pedido_id = self.scope['url_route']['kwargs']['pedido_id']
        self.group_name = f'pedido_{pedido_id}'

        # Agregar al grupo
        await self.channel_layer.group_add(
            self.group_name,
            self.channel_name
        )

        await self.accept()

    async def disconnect(self, close_code):
        # Eliminar del grupo
        await self.channel_layer.group_discard(
            self.group_name,
            self.channel_name
        )

    # Manejar mensajes enviados al grupo
    async def pedido_listo(self, event):
        message = event['message']

        # Enviar el mensaje al WebSocket
        await self.send(text_data=json.dumps({
            'message': message
        }))
