

from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', views.index, name='index'),
    path('inicio-sesion/', views.inicio_sesion, name='inicio_sesion'),
    path('registrarse/', views.registrarse, name='registrarse'),
    path('pagina-principal/', views.pagina_principal, name='pagina_principal'),  
    path('menu/', views.menu_view, name='menu'),
    path('anadir_plato/', views.anadir_plato, name='anadir_plato'),
    path('eliminar-producto/<int:producto_id>/', views.eliminar_producto, name='eliminar_producto'),
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
