

from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', views.index, name='index'),
    path('inicio-sesion/', views.inicio_sesion, name='inicio_sesion'),
    path('pagina-principal/', views.pagina_principal, name='pagina_principal'),  # Asegúrate de que esta URL redirige correctamente.
    path('menu/', views.menu_view, name='menu'),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
