from django import forms
from django.contrib.auth.models import User
from .models import PefilUsuario


class PefilUsuarioForm(forms.ModelForm):
    class Meta():
        model = PefilUsuario
        fields = ('foto_perfil',)
        labels = {
            'foto_perfil' : 'Foto de perfil'
        }

class RegistrarForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ('username', 'email', 'password')
        labels = {
            'username' : 'Nombre de usuario',
            'email' : 'Correo',
            'password': 'Contraseña'
        }
        help_texts = {
           'username': '',
        }
        error_messages = {
            'username': {
                'max_length': 'Máximo 150 carácteres',
                'required': 'Requerido'
            },
            'password': {
                'required': 'Requerido'
            },
        }
    
    def __init__(self, *args, **kwargs):
        super(RegistrarForm, self).__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.update({'class': 'form-control'})
        self.fields['password'].widget.attrs.update({'class': 'form-control'})
        self.fields['email'].widget.attrs.update({'class': 'form-control'})