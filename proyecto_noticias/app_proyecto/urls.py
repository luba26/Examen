from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

app_name = 'app_proyecto'

urlpatterns = [
    path('actualidad', views.actualidad, name='actualidad'),
    path('api_de_prueba/',views.api_de_prueba, name='api'),
    path('Bad_Bunny/', views.Bad_Bunny, name='Bad_Bunny'),
    path('cat_animales/', views.animales, name='animales'),
    path('cat_deportes/', views.deportes, name='deportes'),
    path('cat_ocio/', views.ocio, name='ocio'),
    path('cat_salud/', views.salud, name='salud'),
    path('cat_tecnologia/', views.tecnologia, name='tecnologia'),
    path('Confirmacion/', views.Confirmacion, name='confirmacion'),
    path('Contactanos/', views.Contacto, name='contacto'),
    path('dia_gato/', views.dia_gato, name='gato'),
    path('Formulario/', views.Formulario, name='formulario'),
    path('hitman/', views.hitman, name='hitsman'),
    path('index/', views.index, name='home'),
    path('login/', views.login, name='login'),
    path('narco_gato/', views.narco_gato, name='gato2'),
    path('NBA/', views.NBA, name='NBA'),
    path('Noticia_nasa/', views.NASA, name='Nasa'),
    path('noticia_titanic/', views.noticia_titanic, name='titanic'),
    path('Noticia2/', views.Noticia2, name='noticia2'),
    path('ps5/', views.ps5, name='ps5'),
    path('registro/', views.registro, name='registro'),
    path('SALUD1/', views.SALUD1, name='salud'),
    path('salud2/', views.SALUD2, name='salud2'),
    path('salud3/', views.salud3, name='salud3'),
    path('switch/', views.switch, name='switch'),
    path('tecno1/', views.tecno1, name='tecno1'),
    path('tecno2/', views.tecno2, name='tecno2'),
    path('tecno3/', views.tecno3, name='tecno3'),
    path('Universidad_Catolica/', views.Universidad_Catolica, name='Cato'),
    path('Universidad_de_Chile/', views.Universidad_de_Chile, name='u_chile'),
    path('', views.PostListView.as_view(), name='api'),
    path('detalle/<int:pk>', views.PostDetailView.as_view(), name='detalle'),
    path('crear', views.post_crear, name='crear'),
]
