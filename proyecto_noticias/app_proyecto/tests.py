from django.test import TestCase, Client
from .models import Post
from django.contrib.auth.models import User
from django.contrib.auth import login
from .forms import PostForm
from django.urls import reverse
import datetime

# Create your tests here.


class BlogTest(TestCase):
    def setUp(self):
        self.cliente = Client()
        self.user = None
        try:
            self.user = User.objects.get(username='hal')
        except User.DoesNotExist:
            self.user = User.objects.create_user('hal', password='hal')

        post1 = PostForm(data={'autor': self.user.pk, 'titulo': 'titulo1',
                            'contenido': 'texto'})
        post1.save()

    def test_crear_post(self):
        client = Client()
        fecha = 'fecha'
        post2 = PostForm(data={'autor': self.user.pk, 'titulo': 'titulo2',
                               'contenido': 'texto', 'fecha_publicacion': fecha})
        self.assertTrue(post2.is_valid(),post2.errors)

    def test_buscar_post(self):
        lista_post = Post.objects.filter(titulo='titulo1')
        self.assertEqual(1, len(lista_post), 'No existe el post titulo1')