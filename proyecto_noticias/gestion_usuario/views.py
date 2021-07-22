from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from .forms import RegistrarForm, PefilUsuarioForm

def usuario_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('app_proyecto:api'))


def usuario_login(request):
    if request.user.is_authenticated:
        return HttpResponseRedirect(reverse('app_proyecto:api'))
    else:
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = authenticate(username=username, password=password)
            if user:
                if user.is_active:
                    login(request, user)
                    return HttpResponseRedirect(reverse('app_proyecto:api'))
                else:
                    return HttpResponse("Tu cuenta está inactiva.")
            else:
                print("username: {} - password: {}".format(username, password))
                return HttpResponse("Datos inválidos")
        else:
            return render(request, 'gestion_usuarios/login.html', {})

def registrar(request):
    registrado = False
    if request.method == 'POST':
        user_form = RegistrarForm(data=request.POST)
        profile_form = PefilUsuarioForm(data=request.POST)
        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()
            profile = profile_form.save(commit=False)
            profile.user = user
            if 'foto_perfil' in request.FILES:
                profile.foto_perfil = request.FILES['foto_perfil']
            profile.save()
            registrado = True
        else:
            print(user_form.errors, profile_form.errors)
    else:
        user_form = RegistrarForm()
        profile_form = PefilUsuarioForm()

    return render(request, 'gestion_usuarios/registrar.html',
                  {'user_form': user_form,
                   'profile_form': profile_form,
                   'registrado': registrado})
