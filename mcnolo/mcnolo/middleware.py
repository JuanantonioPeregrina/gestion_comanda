from django.utils.deprecation import MiddlewareMixin
from django.urls import reverse_lazy

# Verificar si la solicitud es para el administrador
def is_admin_request(request):
    return request.path.startswith(('/admin/'))

class AdminSessionMiddleware(MiddlewareMixin):
    def process_request(self, request):
        # Verificar si la sesión está disponible antes de acceder a ella
        if hasattr(request, 'session') and is_admin_request(request):
            # Cambiar el nombre de la cookie de sesión para la administración
            request.session.cookie_name = 'admin_sessionid'
            # Cambiar el nombre de la cookie CSRF para la administración
            request.META['CSRF_COOKIE_NAME'] = 'admin_csrftoken'


