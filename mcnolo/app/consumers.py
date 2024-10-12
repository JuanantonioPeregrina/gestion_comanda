from channels.generic.websocket import AsyncWebsocketConsumer
import json

class PedidoConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.pedido_id = self.scope['url_route']['kwargs']['pedido_id']
        self.pedido_group_name = f'pedido_{self.pedido_id}'

        # Unirse al grupo del pedido
        await self.channel_layer.group_add(
            self.pedido_group_name,
            self.channel_name
        )
        await self.accept()

    async def disconnect(self, close_code):
        # Salir del grupo del pedido
        await self.channel_layer.group_discard(
            self.pedido_group_name,
            self.channel_name
        )

    async def pedido_listo(self, event):
        message = event['message']

        # Enviar el mensaje al WebSocket
        await self.send(text_data=json.dumps({
            'message': message
        }))
 