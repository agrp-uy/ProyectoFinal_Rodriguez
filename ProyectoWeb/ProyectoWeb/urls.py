"""
URL configuration for ProyectoWeb project.

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
from django.urls import path
from AppWeb.views import *
from django.conf import settings
from django.conf.urls.static import static

    

urlpatterns = [
    path('admin/', admin.site.urls),

    #URLs generales
    path('', InicioView.as_view(), name='Inicio'),
    path('inicio/', InicioView.as_view(), name='inicio'),
    path('carta/', CartaView.as_view(), name='carta'),
    path('pedido/', PedidoView.as_view(), name='pedido'),
    path('about/', AboutView.as_view(), name='about'),

    #URLs de los modelos creados (R)
    path('comida/', ComidaView.as_view(), name='comida'),
    path('bebida/', BebidaView.as_view(), name='bebida'),
    path('guarnicion/', GuarnicionView.as_view(), name='guarnicion'),
    path('postre/', PostreView.as_view(), name='postre'),

    #URLs para agregar elementos (C)
    path('agregarComida/', AgregarComida.as_view(), name='agregarComida'),
    path('agregarBebida/', AgregarBebida.as_view(), name='agregarBebida'),
    path('agregarGuarnicion/', AgregarGuarnicion.as_view(), name='agregarGuarnicion'),
    path('agregarPostre/', AgregarPostre.as_view(), name='agregarPostre'),

    #URLs para editar elementos (U)
    path('actualizarComida/<int:pk>/', ActualizarComida.as_view(), name='actualizarComida'),
    path('actualizarBebida/<int:pk>/', ActualizarBebida.as_view(), name='actualizarBebida'),
    path('actualizarGuarnicion/<int:pk>/', ActualizarGuarnicion.as_view(), name='actualizarGuarnicion'),
    path('actualizarPostre/<int:pk>/', ActualizarPostre.as_view(), name='actualizarPostre'),

    #URLs para eliminar elementos (D)
    path('eliminarComida/<int:pk>/', EliminarComida.as_view(), name='eliminarComida'),
    path('eliminarBebida/<int:pk>/', EliminarBebida.as_view(), name='eliminarBebida'),
    path('eliminarGuarnicion/<int:pk>/', EliminarGuarnicion.as_view(), name='eliminarGuarnicion'),
    path('eliminarPostre/<int:pk>/', EliminarPostre.as_view(), name='eliminarPostre'),

    #URLs para buscar elementos
    path('buscarComida/', buscarComida, name='Buscar Comida'), 
    path('buscarBebida/', buscarBebida, name='Buscar Bebida'),
    path('buscarGuarnicion/', buscarGuarnicion, name='Buscar Guarnicion'),
    path('buscarPostre/', buscarPostre, name='Buscar Postre'),

    #URLs para resultados de busqueda:
    path('resultadosComida/', resultadosComida, name='Resultados Comida'),
    path('resultadosBebida/', resultadosBebida, name='Resultados Bebida'),
    path('resultadosGuarnicion/', resultadosGuarnicion, name='Resultados Guarnicion'),
    path('resultadosPostre/', resultadosPostre, name='Resultados Postre'),

    #URLs para manejo de usuarios
    path('login/', user_login, name='Login'),
    path('signup/', user_signup, name='Signup'),
    path('logout/', user_logout, name='Logout'),

    #URLs para manejo de perfiles
    path('editarPerfil/', editar_perfil, name='Editar Perfil'),
    path('agregarAvatar/', agregar_avatar, name='Agregar Avatar'),

    #URLs varias
    path('accesoDenegado/', acceso_denegado, name='accesoDenegado'),
    path('enConstruccion/', en_construccion, name='enConstruccion'),
    

]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
