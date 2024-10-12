from django.urls import path
from . import consumers

websocket_urlpatterns = [
    path(r'ws/pedido/(<int:pedido_id>/', consumers.PedidoConsumer.as_asgi()),
]
