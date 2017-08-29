from django.shortcuts import render

from gestion_usuarios.forms import *
from django.core.urlresolvers import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DetailView
from django.views.generic.edit import *
from gestion_usuarios.models import Usuario
from django.contrib.auth.models import User
from django.contrib import messages



class RegistroUsuario(CreateView):
    model = Usuario
    template_name = "gestion_usuarios/usuario_form.html"
    form_class = RegistroUsuarioForm
    success_msg = "Usuario creado exitosamente"
    success_url = reverse_lazy('gestion_usuarios:listar_usuario')

class EditarUsuario(UpdateView):
    model = Usuario
    form_class = UsuarioUpdateForm
    success_msg = "Perfil actualizado exitosamente"

    def get_success_url(self):
        return reverse_lazy('gestion_usuarios:detail', kwargs={'pk': self.object.id})

    def form_valid(self, form):
        messages.success(self.request, self.success_msg)
        return super(EditarUsuario, self).form_valid(form)

class VerUsuario(DetailView):
    model = Usuario
    template_name = 'gestion_usuarios/usuario_detail.html'

    def get_object(self, queryset=None):
        obj = Usuario.objects.get(id=self.kwargs['pk'])
        return obj


class ListarUsuario(ListView):
    model = Usuario

    def get_context_data(self, **kwargs):
        context = super(ListarUsuario, self).get_context_data(**kwargs)
        context['count'] = self.get_queryset().count()
        return context