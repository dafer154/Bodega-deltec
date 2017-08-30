from django.conf.urls import url
from django.contrib.auth.views import password_change, password_change_done
from django.conf import settings
from django.conf.urls.static import static


from .views import AsignarRecurso, TransferirRecurso, UsuarioRecurso

urlpatterns = [
    url(r'^asignar-recurso/(?P<pk>\d+)$', AsignarRecurso.as_view(), name='asignar_recurso'),
    url(r'^usuario-recurso/(?P<pk>\d+)$', UsuarioRecurso.as_view(), name='usuario_recurso'),
    url(r'^transferir-recurso/(?P<pk_envia>\d+)/(?P<pk_recibe>\d+)', TransferirRecurso.as_view(), name='transferir_recurso'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

