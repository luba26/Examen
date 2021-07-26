from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from .models import Post
from django.utils import timezone
from django.urls import reverse
from .forms import PostForm
from django.views.generic import DetailView, ListView
# Create your views here.

def actualidad (request):
    return HttpResponse('actualidad.html', {})
def api_de_prueba(request):
    return render(request, 'app_proyecto/api_de_prueba.html',{})
def Bad_Bunny(request):
    return render(request, 'app_proyecto/Bad_Bunny.html',{})
def actualidad(request):
    return render(request, 'app_proyecto/cat_actualidad.html',{})
def animales(request):
    return render(request, 'app_proyecto/cat_animales.html',{})
def deportes(request):
    return render(request, 'app_proyecto/cat_deportes.html',{})
def ocio(request):
    return render(request, 'app_proyecto/cat_ocio.html',{})
def salud(request):
    return render(request, 'app_proyecto/cat_salud.html',{})
def tecnologia(request):
    return render(request, 'app_proyecto/cat_tecnologia.html',{})
def Confirmacion(request):
    return render(request, 'app_proyecto/Confirmacion.html',{})
def Contacto(request):
    return render(request, 'app_proyecto/Contactanos.html',{})
def dia_gato(request):
    return render(request, 'app_proyecto/dia_gato.html',{})
def Formulario(request):
    return render(request, 'app_proyecto/Formulario.html',{})
def hitman(request):
    return render(request, 'app_proyecto/hitman.html',{})
def index(request):
    return render(request, 'app_proyecto/index.html',{})
def login(request):
    return render(request, 'app_proyecto/login.html',{})
def narco_gato(request):
    return render(request, 'app_proyecto/narco.html',{})
def NBA(request):
    return render(request, 'app_proyecto/NBA.html',{})
def NASA(request):
    return render(request, 'app_proyecto/noticia_nasa.html',{})
def noticia_titanic(request):
    return render(request, 'app_proyecto/noticia_titanic.html',{})
def Noticia2(request):
    return render(request, 'app_proyecto/Noticia2.html',{})
def ps5(request):
    return render(request, 'app_proyecto/ps5.html',{})
def registro(request):
    return render(request, 'app_proyecto/registro.html',{})
def SALUD1(request):
    return render(request, 'app_proyecto/SALUD1.html',{})
def SALUD2(request):
    return render(request, 'app_proyecto/salud2.html',{})
def salud3(request):
    return render(request, 'app_proyecto/salud3.html',{})
def switch(request):
    return render(request, 'app_proyecto/switch.html',{})
def tecno1(request):
    return render(request, 'app_proyecto/tecno1.html',{})
def tecno2(request):
    return render(request, 'app_proyecto/tecno2.html',{})
def tecno3(request):
    return render(request, 'app_proyecto/tecno3.html',{})
def Universidad_Catolica(request):
    return render(request, 'app_proyecto/Universidad_Catolica.html',{})
def Universidad_de_Chile(request):
    return render(request, 'app_proyecto/Universidad_de_Chile.html',{})

class PostListView(ListView):
    model = Post
    template_name = "app_proyecto/api.html"


def post_lista(request):
    posts = None
    if request.user.is_authenticated:
        posts = Post.objects.all().order_by('fecha_publicacion')
    else:
        posts = Post.objects.filter(
            fecha_publicacion__lte=timezone.now()).order_by('fecha_publicacion')
    error = None
    if 'error' in request.session:
        error = request.session['error']
        del request.session['error']

    return render(request, 'app_proyecto/api.html', {'posts': posts, 'error': error})


def post_crear(request):
    if not request.user.is_authenticated:
        request.session['error'] = "Sin autorización para agregar nuevos post"
        return render(request, 'gestion_usuarios/login.html', {})

    if request.method == 'GET':
        post_form = PostForm(initial={'autor': request.user.pk})
        return render(request, 'app_proyecto/post_crear.html', {'post_form': post_form})
    elif request.method == 'POST':
        message = ""
        try:
            post_form = PostForm(data=request.POST)
            if post_form.is_valid():
                # post.fecha_publicacion = lambda fecha_publicacion : None if fecha_publicacion == "" else request.POST.get('fecha_publicacion')
                post = post_form.save()
                file = request.FILES['imagen']
                ext = file.name.split(".")[-1]
                file.name = str(post.pk) + "." + ext
                post.imagen = file
                post.save()
                message = "la publicacion fue guardada"
                return HttpResponseRedirect(reverse('app_proyecto:detalle', args=(post.pk,)))
            else:
                message = post_form.errors
                return render(request, 'app_proyecto/post_crear.html', {'message': message, 'post_form': post_form})
        except Exception as e:
            message = "Error al guardar la publicación: " + str(e)
            return render(request, 'app_proyecto/post_crear.html', {'message': message})
    else:
        response = HttpResponse('Método no permitido')
        response.status_code = 405
        return response


class PostDetailView(DetailView):
    model = Post
    template_name = "app_proyecto/post_detalle.html"
    


def post_detalle(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    if request.method == 'POST':
        post.publish()

    try:
        return render(request, 'app_proyecto/post_detalle.html', {'post': post})
    except Exception as e:
        response = HttpResponse("Error al guardar la publicación: " + str(e))
        response.status_code = 404
        return response
