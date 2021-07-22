from django.db import models
from django.contrib.auth.models import User


class PefilUsuario(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    foto_perfil = models.ImageField(upload_to='foto_perfil', blank=True)

    def __str__(self):
        return self.user.username