from django.db import models
from django.db.models.deletion import CASCADE
from django.utils import timezone
# Create your models here.

class Noticias(models.Model):
    name = models.CharField(max_length=300 ) 
    categoria= models.CharField(max_length=40)
    description = models.CharField(max_length=300)

    def _str_(self):
        return self.name
    class Meta:
        db_table = 'Noticias'
        ordering = ['-id']


class Cliente (models.Model):
    name = models.CharField(max_length=300)
    telephone = models.IntegerField()
    email = models.EmailField(max_length= 100)


class Category(models.Model):
    name =models.CharField(max_length=300)
    featured = models.BooleanField(max_length=300, default=False)
    noticias = models.ManyToManyField(Noticias)
    cliente = models.ForeignKey(Cliente, on_delete=CASCADE)


    def _str_(self):
        return self.name
    class Meta:
        db_table = 'categories'
        verbose_name = 'Categoría'
        verbose_name_plural = 'Categorías'
        ordering = ['-id']

class Post(models.Model):
    autor = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    titulo = models.CharField(max_length=200)
    contenido = models.TextField()
    fecha_creacion = models.DateTimeField(default=timezone.now)
    fecha_publicacion = models.DateTimeField(blank=True, null=True)
    imagen = models.FileField(blank=True, null=True, upload_to="app_proyecto")


    def publish(self):
        self.fecha_publicacion = timezone.now()
        self.save()

    def __str__(self):
        return self.titulo

