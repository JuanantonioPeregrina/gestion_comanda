

from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('', views.index, name='index'),
    path('invitado/', views.invitado, name='invitado'),  # Ruta para invitados
    path('inicio-sesion/', views.inicio_sesion, name='inicio_sesion'),
    path('registrarse/', views.registrarse, name='registrarse'),
    path('pagina-principal/', views.pagina_principal, name='pagina_principal'),  
    path('menu/', views.menu_view, name='menu'),
    path('anadir_plato/', views.anadir_plato, name='anadir_plato'),
    path('eliminar-producto/<int:producto_id>/', views.eliminar_producto, name='eliminar_producto'),
    path('cambiar_visibilidad_producto/<int:producto_id>/', views.cambiar_visibilidad_producto, name='cambiar_visibilidad_producto'),
    path('logout/', auth_views.LogoutView.as_view(next_page='index'), name='logout'),
    path('finalizar-compra/', views.finalizar_compra, name='finalizar_compra'),
    path('obtener-estado-pedido/<int:pedido_id>/', views.obtener_estado_pedido, name='obtener_estado_pedido'),
    # path('ver_carrito/', views.ver_carrito, name='ver_carrito'),
    #path('carrito/', views.ver_carrito, name='carrito'),
    path('comprobar_oferta' , views.comprobar_oferta, name='comprobar_oferta'),
    path('change_username/', views.change_username, name='change_username'),
    path('change_image/', views.change_image, name='change_image'),
    ]
    



if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
