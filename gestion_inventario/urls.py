from django.conf.urls import url
from django.contrib.auth.views import password_change, password_change_done
from django.conf import settings
from django.conf.urls.static import static


from .views import CrearRecurso, EditarRecurso, VerRecurso, ListarRecurso
urlpatterns = [
    url(r'^crear-recurso$', CrearRecurso.as_view(), name='crear_recurso'),
    url(r'^editar-recurso$', EditarRecurso.as_view(), name='editar_recurso'),
    url(r'^listar-recurso$', ListarRecurso.as_view(), name='listar_recursos'),
    url(r'^ver-detalle$', VerRecurso.as_view(), name='ver_recurso'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

