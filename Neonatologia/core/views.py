from django.shortcuts import render, redirect
from .models import UserMatrona
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout

# Create your views here.
def inicio(request):
    return render(request,'core/inicio.html',{})

def conozcanos(request):
    return render(request,'core/conozcanos.html',{})

def padreslogin(request):
    return render(request,'core/padreslogin.html',{})

def lmatrona(request):
    rut_usuario = request.GET.get('RutMatrona')
    contrasena = request.GET.get('ContrasenaMatrona')
    matrona = UserMatrona.objects.all()
    if UserMatrona.objects.filter(rut = rut_usuario):
        if UserMatrona.objects.filter(password = contrasena):
            matrona = UserMatrona.objects.filter(rut = rut_usuario)
            return matrona(request, matrona)
    return render(request,'core/lmatrona.html')

def logout_view(request):
 logout(request)
 return redirect('/')

@login_required
def matrona(request,matrona):
    return render(request,'core/matrona.html',{'matrona':matrona})

