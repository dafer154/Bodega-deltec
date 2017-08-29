from django.conf.urls import url
from django.contrib.auth.views import password_change, password_change_done
from django.conf import settings
from django.conf.urls.static import static


from .views import RegistroUsuario, EditarUsuario, ListarUsuario, VerUsuario

urlpatterns = [
    url(r'^crear-usuario$', RegistroUsuario.as_view(), name='crear_usuario'),
    url(r'^editar-usuario$', EditarUsuario.as_view(), name='editar_usuario'),
    url(r'^listar-usuario$', ListarUsuario.as_view(), name='listar_usuario'),
    url(r'^ver-detalle$', VerUsuario.as_view(), name='ver_usuario'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)



