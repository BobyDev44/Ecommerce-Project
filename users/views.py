from django.shortcuts import render, redirect
from .forms import *
from django.contrib import messages
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import AuthenticationForm

# Create your views here.

def home(request): #ESTO DEBE ELIMINAR CUANDO LO VAYA A USAR JUNTO CON EL HTML, AUNQ NO ES NECESARIO
    if request.user.is_authenticated:
        return render (request, "users/home.html")
    else:
        return redirect("/users/iniciarsesion/")
    
def registro(request):
    if request.method == "POST":
        form = CrearUser(request.POST)
        if form.is_valid():
            usuario = form.save()
            usuario.save()
            login(request, usuario)
            return redirect("/")
        else:
            #messages.error(request, "Ha ocurrido un error, revisa los campos")
            return render (request, "users/registro.html", {"form":form})
    else:
        form = CrearUser()
    return render (request, "users/registro.html", {"form":form})

def registrosuper(request):
    if request.method == "POST":
        form = CrearSuperUser(request.POST)
        if form.is_valid():
            form.save()
            return redirect("/admin/")
        else:
            messages.error(request, "Ha ocurrido un error, revisa los campos")
            return render (request, "users/superuser.html", {"form":form})
    form = CrearUser()
    return render (request, "users/superuser.html", {"form":form})

def iniciarsesion(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            nombre_usuario = form.cleaned_data.get("username")
            contra = form.cleaned_data.get("password")
            usuario = authenticate(username = nombre_usuario, password = contra)
            if usuario is not None:
                login(request, usuario)
                return redirect("/") #ESTO DEBE CAMBIAR DONDE LO VAYA A USAR
            else:
               messages.error(request, "El usuario no existe")
        else:
            messages.error(request, "Informacion incorrecta")
    form = AuthenticationForm()
    return render(request, "users/iniciarsesion.html", {"form":form})

def cerrarsesion(request):
    logout(request)
    return redirect("/users/iniciarsesion/")