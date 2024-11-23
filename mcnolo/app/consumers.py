from channels.generic.websocket import AsyncWebsocketConsumer
import json

class PedidoConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        # Determinar si es un invitado o un usuario autenticado
        self.invitado_id = self.scope['url_route']['kwargs'].get('invitado_id')

        if self.invitado_id:
            self.group_name = f'invitado_{self.invitado_id}'  # Grupo genérico para invitados
        else:
            self.pedido_id = self.scope['url_route']['kwargs'].get('pedido_id')
            self.group_name = f'pedido_{self.pedido_id}'

        # Unirse al grupo WebSocket
        await self.channel_layer.group_add(self.group_name, self.channel_name)
        await self.accept()

    async def disconnect(self, close_code):
        await self.channel_layer.group_discard(self.group_name, self.channel_name)

    async def pedido_listo(self, event):
        message = event['message']
        await self.send(text_data=json.dumps({'message': message}))
