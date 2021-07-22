from django.conf.urls import url
from . import views
app_name = 'gestion_usuarios'

urlpatterns = [
    url('registrar/', views.registrar, name='registrar'),
    url('login/', views.usuario_login, name='login'),
    url('logout/', views.usuario_logout, name='logout'),
]