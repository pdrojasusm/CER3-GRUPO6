from django.shortcuts import render

# Create your views here.
def inicio(request):
    #return HttpResponse("<h1>Hola Mundo</h1>")
    return render(request,'core/inicio.html')