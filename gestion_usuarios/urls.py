from django.conf.urls import url
from django.contrib.auth.views import password_change, password_change_done

from .views import RegistroUsuario, EditarUsuario

urlpatterns = [
    url(r'^crear-usuario$', RegistroUsuario.as_view(), name='crear_usuario'),
    url(r'^editar-usuario$', EditarUsuario.as_view(), name='editar_usuario'),
]




