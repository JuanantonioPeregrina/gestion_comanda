# tests.py

from django.test import TestCase
from .models import Pedido
from django.contrib.auth.models import User

class PedidoModelTests(TestCase):

    def setUp(self):
        # Crear un usuario para asociar con el pedido
        self.user = User.objects.create_user(username='testuser', password='testpassword')

    def test_crear_pedido(self):
        # Crear un pedido asociado al usuario
        pedido = Pedido.objects.create(usuario=self.user, total=50.00, estado='pendiente')

        # Verificar que el pedido se haya guardado correctamente
        self.assertEqual(pedido.usuario.username, 'testuser')
        self.assertEqual(pedido.total, 50.00)
        self.assertEqual(pedido.estado, 'pendiente')