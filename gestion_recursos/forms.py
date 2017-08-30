from django import forms
from gestion_usuarios.models import Usuario, User
from gestion_inventario.models import Recursos
from .models import Asignar_recurso
from django.db.models import Min


class AsignarRecursoForm(forms.ModelForm):
    #pizza = forms.ModelChoiceField(queryset=Pizza.objects.annotate(min_cantidad=Min('ingredientes__cantidad_disponible')).filter(min_cantidad__gte=1))
    class Meta(object):
        model = Asignar_recurso
        fields = ['recursos']
        exclude = ['usuario']