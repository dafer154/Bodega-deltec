from django import forms
from gestion_usuarios.models import Usuario, User
from gestion_inventario.models import Recursos
from .models import Asignar_recurso
from django.db.models import Min


class AsignarRecursoForm(forms.ModelForm):
    class Meta(object):
        model = Asignar_recurso
        fields = ['recursos']
        exclude = ['usuario']


class TransferirRecursoForm(forms.ModelForm):
    def __init__(self, pk_recibe=None, pk_envia=None, *args, **kwargs):

        super(TransferirRecursoForm, self).__init__(*args, **kwargs)
        self.fields['recursos']= forms.ModelChoiceField(queryset=Asignar_recurso.objects.filter(usuario=pk_envia))

    class Meta(object):
        model = Asignar_recurso
        fields = ['recursos']
        exclude = ['usuario']