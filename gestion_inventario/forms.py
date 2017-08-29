from django import forms
from .models import Asignar_recursos, Recursos
from django.contrib.auth.forms import UserCreationForm


class CrearRecursoForm(forms.ModelForm):
    class Meta:
        model = Recursos
        fields = ('categoria', 'nombre', 'codigo', 'marca', 'serie')

class RecursoUpdateForm(forms.ModelForm):
    class Meta:
        model = Recursos
        fields = ('categoria', 'nombre', 'codigo', 'marca', 'serie')


class AsignarRecursoForm(forms.ModelForm):
    class Meta:
        model = Asignar_recursos
        fields = ('usuario', 'recursos')
