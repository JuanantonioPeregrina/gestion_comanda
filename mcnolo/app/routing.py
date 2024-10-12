from django.urls import re_path
from . import consumers

websocket_urlpatterns = [
    re_path(r'ws/pedido/(?P<pedido_id>\d+)/$', consumers.PedidoConsumer.as_asgi()),
]
