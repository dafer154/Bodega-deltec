from django.db import models
from django.core.urlresolvers import reverse
from gestion_usuarios.models import Usuario


class Recursos(models.Model):

    categorias = (
        ('A', 'Aseo'),
        ('H', 'Herramientas'),
        ('O', 'Oficina'),
    )

    categoria = models.CharField(max_length=1, choices=categorias, null=True)
    nombre = models.CharField(verbose_name="Nombre", max_length=40)
    codigo = models.CharField(verbose_name="Codigo", max_length=40)
    marca = models.CharField(verbose_name="Marca", max_length=40)
    serie = models.CharField(verbose_name="Serie", max_length=40)
    date_joined = models.DateField(auto_now_add=True)

    def __str__(self):
        return str(self.nombre)


class Asignar_recursos(models.Model):

    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    recursos = models.ManyToManyField(Recursos, blank=True, null=True)
    date_joined = models.DateField(auto_now_add=True)

    def __str__(self):
        return str(self.nombre)
