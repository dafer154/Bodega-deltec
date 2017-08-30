from django.conf.urls import url
from django.contrib.auth.views import password_change, password_change_done
from django.conf import settings
from django.conf.urls.static import static


from .views import AsignarRecurso

urlpatterns = [
    url(r'^asignar-recurso/(?P<pk>\d+)$', AsignarRecurso.as_view(), name='asignar_recurso'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

