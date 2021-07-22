from django.test import TestCase, Client
from .models import PefilUsuario
from django.contrib.auth.models import User
from .forms import RegistrarForm, PefilUsuario
from django.urls import reverse

# Create your tests here.


class GestionUsuarioTest(TestCase):
    def setUp(self):
        self.cliente = Client()
        User.objects.create_user('seba',password='seba')


    def test_login(self):
        response = self.cliente.post(
            reverse('gestion_usuarios:login'), {'username': 'seba', 'password': 'seba'})
        self.assertEqual(response.status_code, 302, 'No es el código correcto')