"""Neonatologia URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from core import views
from core.api.router import router_recien_nacido
urlpatterns = [
    path('',views.inicio,name='inicio'),
    path('conozcanos/',views.conozcanos,name='conozcanos'),
    path('login/',views.lmatrona,name='lmatrona'),
    path('matrona/',views.matrona,name='matrona'),
    path('logout/',views.logout_request,name='logout'),
    path('padreslogin/',views.padreslogin,name='padreslogin'),
    path('BienvenidaPadre/',views.BienvenidaPadre,name='BienvenidaPadre'),
    path('admin/', admin.site.urls),
    path('api/',include(router_recien_nacido.urls) )
 

]
