from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.models import User
from django.contrib import messages
from .forms import recien_nacidoForm

# Create your views here.
def inicio(request):
    return render(request,'core/inicio.html',{})

def conozcanos(request):
    return render(request,'core/conozcanos.html',{})

def lmatrona(request):
    if request.method == 'POST':
        form = AuthenticationForm(request,data=request.POST)
        if form.is_valid():
            usuario = form.cleaned_data.get('username')
            contrasena = form.cleaned_data.get('password')
            user = authenticate(username=usuario,password=contrasena)
            if user is not None:
                login(request,user)
                messages.info(request,f'estas logeado como {usuario}')
                return redirect("core:matrona")
            else:
                messages.error(request,"usuario o contraseña equivocados")
        else:
            messages.error(request,"usuario o contraseña equivocados")

    form = AuthenticationForm()
    return render(request,'core/mlogin.html',{'form':form})

def matrona(request):
    return render(request,'core/matrona.html',{})

def logout_request(request):
    logout(request)
    return redirect('core:lmatrona')

def padreslogin(request):
    logout(request)
    return render(request,'core/padreslogin.html',{})
    
def BienvenidaPadre(request):
    return render(request,'core/BienvenidaPadre.html',{})


def recien_nacido(request):
    data = {
        'form':recien_nacidoForm()
    }
    if request.method == 'POST':
        formulario = recien_nacidoForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            data["mensaje"]="contacto guardado"
        else:
            data["form"]= formulario
            
    return render(request, 'core/matrona.html', data)