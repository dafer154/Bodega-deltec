from django.db import models
from gestion_usuarios.models import Usuario, User
from gestion_inventario.models import Recursos

# Create your models here.
class Asignar_recursos(models.Model):

    usuario = models.ForeignKey(Usuario)
    recursos = models.ManyToManyField(Recursos)
    date_joined = models.DateField(auto_now_add=True)


class Asignar_recurso(models.Model):

    usuario = models.ForeignKey(Usuario)
    recursos = models.ForeignKey(Recursos, unique=True)
    date_joined = models.DateField(auto_now_add=True)

    def __str__(self):
        return str(self.recursos)