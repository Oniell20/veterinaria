"""
URL configuration for veterinaria project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.urls import path, include # Importante: incluye 'include'
from django.contrib.auth import views as auth_views # Importar vistas de auth
from proyecto import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.bienvenida, name='bienvenida'),
    path('bienvenida/', views.bienvenida, name='bienvenida_directa'),

    # Autenticación
    # Django buscará automáticamente 'registration/login.html'
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('registro/', views.registro_view, name='registro'),

    # Módulos del sistema (protegidos)
    path('dashboard/', views.dashboard, name='dashboard'),
    path('agenda/', views.agenda, name='agenda'),
    path('pacientes/', views.pacientes, name='pacientes'),
    path('inventario/', views.inventario, name='inventario'),
    path('peluqueria/', views.peluqueria, name='peluqueria'),
    path('caja/', views.caja, name='caja'),
    path('facturacion/', views.facturacion, name='facturacion'),
    path('clientes/', views.clientes, name='clientes'),
    path('reportes/', views.reportes, name='reportes'),
]


