from django.shortcuts import render
from .models import Asignar_recurso
from gestion_usuarios.models import Usuario
from django.views.generic import ListView, CreateView, UpdateView, DetailView
from gestion_recursos.forms import *
from django.core.urlresolvers import reverse_lazy
from django.contrib import messages
# Create your views here.

class AsignarRecurso(CreateView):
    model = Asignar_recurso
    template_name = "gestion_recursos/asignarRecurso_form.html"
    form_class = AsignarRecursoForm
    success_msg = "Recurso registrado exitosamente"
    success_url = reverse_lazy('gestion_inventario:listar-recursos')

    def form_valid(self, form):
        usuarioId = self.kwargs['pk']
        usuario = Usuario.objects.get(pk=usuarioId)

        asignar_recurso = form.save(commit=False)
        asignar_recurso.usuario = usuario
        asignar_recurso.save()
        self.success_url = reverse_lazy('gestion_recursos:asignar_recurso', kwargs={'pk': usuarioId})
        return super(AsignarRecurso, self).form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        usuarioId = self.kwargs['pk']
        usuario = Usuario.objects.get(pk=usuarioId)
        print(usuario)
        try:
            context['asignar_recursos'] = Asignar_recurso.objects.all().filter(usuario=usuario)
            print(context['asignar_recursos'])
        except Asignar_recurso.DoesNotExist:
            context['asignar_recursos'] = []
        return context