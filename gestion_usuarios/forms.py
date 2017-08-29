from django import forms
from .models import Usuario
from django.contrib.auth.forms import UserCreationForm

password1 = forms.CharField(label="Contraseña", widget=forms.PasswordInput(attrs={'maxlength': 30, 'class': 'form-control', 'placeholder': ("Contraseña")})) #Nuevo campo
password2 = forms.CharField(label="Contraseña (confirmación)", widget=forms.PasswordInput(attrs={'maxlength': 30, 'class': 'form-control', 'placeholder': ("Confirma tu contraseña")}))
username_ht = "Requerido. 150 o menos carácteres. Solamente letras, dígitos y @/./+/-/_.',"

class RegistroUsuarioForm(UserCreationForm):
    class Meta:
        model = Usuario
        help_texts = {
            'username': username_ht
        }
        exclude = ('is_active', 'last_login', 'user_permissions', 'is_staff', 'date_joined', 'is_superuser',)
        fields = ('first_name', 'last_name', 'username', 'password1', 'password2', 'email', 'genero', 'celular', 'imagen_perfil')

class UsuarioUpdateForm(forms.ModelForm):
    class Meta:
        model = Usuario
        help_texts = {
            'username': username_ht
        }
        exclude = ('is_active', 'last_login', 'groups', 'user_permissions', 'is_staff', 'date_joined', 'is_superuser')
        fields = ('first_name', 'last_name', 'username', 'email', 'genero', 'celular', 'imagen_perfil')
