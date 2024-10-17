# tests.py

from django.test import TestCase
from .models import *
from django.contrib.auth.models import User
from .views import crear_usuario_oferta
from django.core import mail

class PedidoModelTests(TestCase):

    """ 
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
    """
    
    def test_oferta_crear_usuario(self):
        # Crear un usuario con una oferta asociada
        #user = User.objects.create_user(username='testuser', password='testpassword')
        crear_usuario_oferta('testuser@yu', 'testpassword')
        print("Hasta aqui hace")
        user = User.objects.get(username='testuser@yu')
        oferta = Oferta.objects.filter(usuario=user).first()
        self.assertEqual(oferta.codigo, 'testuser@yu_10')
        
        # Verificar que la oferta se haya guardado correctamente
    def test_envia_correo_al_crear_oferta(self):
        email = 'mcnolorestaurante@gmail.com'
        password = 'mcnolorestaurante99'

        crear_usuario_oferta(email, password)
        self.assertEqual(len(mail.outbox), 1)

