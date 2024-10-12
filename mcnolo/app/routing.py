from django.urls import path
from . import consumers
from app.consumers import PedidoConsumer

websocket_urlpatterns = [
    path('ws/pedido/<int:pedido_id>/', consumers.PedidoConsumer.as_asgi()),
]