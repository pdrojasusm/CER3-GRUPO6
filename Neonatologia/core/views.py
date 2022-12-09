from django.shortcuts import render

# Create your views here.
def inicio(request):
    return render(request,'core/inicio.html',{})

def conozcanos(request):
    return render(request,'core/conozcanos.html',{})

def lmatrona(request):
    return render(request,'core/mlogin.html',{})

def matrona(request):
    return render(request,'core/matrona.html',{})