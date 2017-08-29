from django.db import models
from django.core.urlresolvers import reverse


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


