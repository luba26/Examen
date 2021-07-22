from django import forms
from django.contrib.auth.models import User
from .models import Post

class PostForm(forms.ModelForm):
    class Meta():
        model = Post
        fields = ('titulo', 'contenido', 'imagen', 'fecha_publicacion','autor')
        widgets={ 
            'fecha_publicacion': forms.DateInput(attrs={'type':'date'}), 
            'autor':forms.HiddenInput()
            }


    def __init__(self, *args, **kwargs):
        super(PostForm, self).__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs.update({'class': 'form-control'})