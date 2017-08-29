from django.shortcuts import render

from gestion_inventario.forms import *
from django.core.urlresolvers import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DetailView
from django.views.generic.edit import *
from gestion_usuarios.models import Usuario
from .models import Recursos
from django.contrib import messages


class CrearRecurso(CreateView):
    model = Recursos
    template_name = "gestion_inventario/crearRecurso_form.html"
    form_class = CrearRecursoForm
    success_msg = "Recurso registrado exitosamente"
    success_url = reverse_lazy('gestion_inventario:listar-recursos')



class EditarRecurso(UpdateView):
    model = Recursos
    form_class = RecursoUpdateForm
    success_msg = "Recurso actualizado exitosamente"

    def get_success_url(self):
        return reverse_lazy('gestion_inventario:ver_recurso', kwargs={'pk': self.object.id})

    def form_valid(self, form):
        messages.success(self.request, self.success_msg)
        return super(EditarRecurso, self).form_valid(form)

class VerRecurso(DetailView):
    model = Recursos
    template_name = 'gestion_inventario/ver_recurso.html'

    def get_object(self, queryset=None):
        obj = Recursos.objects.get(id=self.kwargs['id'])
        return obj


class ListarRecurso(ListView):
    model = Recursos

    def get_context_data(self, **kwargs):
        context = super(ListarRecurso, self).get_context_data(**kwargs)
        context['count'] = self.get_queryset().count()
        return context


#
# class AsignarRecurso(CreateView):
#     model = Asignar_recursos
#     template_name = "gestion_inventario/asignarRecurso_form.html"
#     form_class = AsignarRecursoForm
#     success_msg = "Recurso asignado exitosamente"
#     success_url = reverse_lazy('usuarios:listar')
#
