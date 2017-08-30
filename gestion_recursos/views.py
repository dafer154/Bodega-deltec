from django.shortcuts import render
from .models import Asignar_recurso
from gestion_usuarios.models import Usuario
from django.views.generic import ListView, CreateView, UpdateView, DetailView, FormView
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

class UsuarioRecurso(ListView):
    model = Usuario
    template_name = "gestion_recursos/usuariosTransferir_list.html"
    def get_context_data(self, **kwargs):

        context = super(UsuarioRecurso, self).get_context_data(**kwargs)
        usuarioId = self.kwargs['pk']
        context['id_url']=usuarioId
        context['count'] = self.get_queryset().count()
        return context

class TransferirRecurso(CreateView):
    model = Asignar_recurso
    template_name = "gestion_recursos/transferirRecurso_form.html"
    form_class = TransferirRecursoForm
    success_msg = "Recurso registrado exitosamente"
    success_url = reverse_lazy('gestion_inventario:listar-recursos')

    def get_form_kwargs(self):
        kwargs = super(TransferirRecurso, self).get_form_kwargs()
        # update the kwargs for the form init method with yours
        kwargs.update(self.kwargs)  # self.kwargs contains all url conf params
        return kwargs

    def form_valid(self, form):
        usuarioEnviaId = self.kwargs['pk_envia']
        usuarioRecibeId = self.kwargs['pk_recibe']

        usuarioEnvia = Usuario.objects.get(pk=usuarioEnviaId)
        usuarioRecibe = Usuario.objects.get(pk=usuarioRecibeId)

        asignar_recurso = form.save(commit=False)
        asignar_recurso.usuario = usuarioRecibe
        asignar_recurso.save()
        self.success_url = reverse_lazy('gestion_recursos:transferir_recurso', kwargs={'pk_envia': usuarioEnviaId})
        return super(AsignarRecurso, self).form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        usuarioId = self.kwargs['pk_recibe']
        usuarioEnviaId = self.kwargs['pk_envia']

        usuarioRecibe = Usuario.objects.get(pk=usuarioId)
        usuarioEnvia = Usuario.objects.get(pk=usuarioEnviaId)
        print(usuarioRecibe)
        try:
            context['asignar_recursos'] = Asignar_recurso.objects.all().filter(usuario=usuarioRecibe)
            context['usuario_envia'] = usuarioEnvia
            context['usuario_recibe'] = usuarioRecibe

            print(context['asignar_recursos'])
        except Asignar_recurso.DoesNotExist:
            context['asignar_recursos'] = []
        return context