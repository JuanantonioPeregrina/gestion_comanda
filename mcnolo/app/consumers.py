from channels.generic.websocket import AsyncWebsocketConsumer
import json

class PedidoConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        # Obtén el pedido_id desde la URL
        self.pedido_id = self.scope['url_route']['kwargs']['pedido_id']
        # Crea un nombre de grupo basado en el pedido_id
        self.pedido_group_name = f'pedido_{self.pedido_id}'
        
        # Únete al grupo de pedidos correspondiente
        await self.channel_layer.group_add(
            self.pedido_group_name,
            self.channel_name
        )

        # Acepta la conexión WebSocket
        await self.accept()

    async def disconnect(self, close_code):
        # Abandona el grupo de pedidos cuando se desconecte
        await self.channel_layer.group_discard(
            self.pedido_group_name,
            self.channel_name
        )

    # Recibe el mensaje 'pedido_listo' desde el grupo
    async def pedido_listo(self, event):
        message = event['message']

        # Envía el mensaje al WebSocket en formato JSON
        await self.send(text_data=json.dumps({
            'message': message
        }))
