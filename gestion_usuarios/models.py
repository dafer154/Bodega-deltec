from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Usuario(User):


    generos = (
        ('M', 'Masculino'),
        ('F', 'Femenino'),
    )

    genero = models.CharField(max_length=1, choices=generos, null=True)
    celular = models.CharField('Celular', max_length=10)
    documento_id = models.CharField('Cédula', max_length=11)
    imagen_perfil = models.ImageField(verbose_name="Imagen de perfil", upload_to='imagenes_perfil/', null=True)

    def __str__(self):
        return User.get_full_name(self)
