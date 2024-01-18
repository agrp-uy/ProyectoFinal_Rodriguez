from django.shortcuts import render
from django.http import HttpResponse
from AppWeb.models import *
from AppWeb.forms import *
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView, TemplateView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from AppWeb.models import Comida, Bebida, Guarnicion, Postre
from AppWeb.forms import ComidaForm, BebidaForm, GuarnicionForm, PostreForm



# Create your views here.


class InicioView(TemplateView):
    template_name = "AppWeb/inicio.html"

class CartaView(TemplateView):
    template_name = "AppWeb/carta.html"

class PedidoView(TemplateView):
    template_name = "AppWeb/pedido.html"

#vistas para crear nuevos objetos (C)
#@login_required #Bloquear acceso a usuarios no registrados
    
class AgregarComida(CreateView):
    model = Comida
    form_class = ComidaForm
    template_name = "AppWeb/agregarComida.html"
    success_url = reverse_lazy('inicio')

class AgregarBebida(CreateView):
    model = Bebida
    form_class = BebidaForm
    template_name = "AppWeb/agregarBebida.html"
    success_url = reverse_lazy('inicio')

class AgregarGuarnicion(CreateView):
    model = Guarnicion
    form_class = GuarnicionForm
    template_name = "AppWeb/agregarGuarnicion.html"
    success_url = reverse_lazy('inicio')

class AgregarPostre(CreateView):
    model = Postre
    form_class = PostreForm
    template_name = "AppWeb/agregarPostre.html"
    success_url = reverse_lazy('inicio')


#Vistas para leer los modelos creados (R)

class ComidaView(ListView):
    model = Comida
    template_name = "AppWeb/comida.html"
    context_object_name = 'comidas'
    ordering = ['nombre']

class BebidaView(ListView):
    model = Bebida
    template_name = "AppWeb/bebida.html"
    context_object_name = 'bebidas'
    ordering = ['nombre']

class GuarnicionView(ListView):
    model = Guarnicion
    template_name = "AppWeb/guarnicion.html"
    context_object_name = 'guarniciones'
    ordering = ['nombre']

class PostreView(ListView):
    model = Postre
    template_name = "AppWeb/postre.html"
    context_object_name = 'postres'
    ordering = ['nombre']


#Vistas para editar los modelos creados (U)


class ActualizarComida(UpdateView):
    model = Comida
    form_class = ComidaForm
    template_name = 'AppWeb/actualizarComida.html'
    success_url = '/comida/'

class ActualizarBebida(UpdateView):
    model = Bebida
    form_class = BebidaForm
    template_name = 'AppWeb/actualizarBebida.html'
    success_url = '/bebida/'

class ActualizarGuarnicion(UpdateView):
    model = Guarnicion
    form_class = GuarnicionForm
    template_name = 'AppWeb/actualizarGuarnicion.html'
    success_url = '/guarnicion/'

class ActualizarPostre(UpdateView):
    model = Postre
    form_class = PostreForm
    template_name = 'AppWeb/actualizarPostre.html'
    success_url = '/postre/'

#Vistas para eliminar los modelos creados (D)

class EliminarComida(DeleteView):
    model = Comida
    template_name = 'AppWeb/eliminarComida.html'
    success_url = '/comida/'

class EliminarBebida(DeleteView):
    model = Bebida
    template_name = 'AppWeb/eliminarBebida.html'
    success_url = '/bebida/'

class EliminarGuarnicion(DeleteView):
    model = Guarnicion
    template_name = 'AppWeb/eliminarGuarnicion.html'
    success_url = '/guarnicion/'

class EliminarPostre(DeleteView):
    model = Postre
    template_name = 'AppWeb/eliminarPostre.html'
    success_url = '/postre/'

#Vistas para los formularios de busqueda:

def buscarComida(request):
    return render(request, "AppWeb/buscarComida.html")

def resultadosComida(request):
    if request.method == 'GET':
        comida_buscada = request.GET['nombre']
        resultados_comida = Comida.objects.filter(nombre__icontains=comida_buscada).order_by('nombre')
        
    return render(request, "AppWeb/buscarComida.html", {'comidas_b':resultados_comida})

def buscarBebida(request):
    return render(request, "AppWeb/buscarBebida.html")

def resultadosBebida(request):
    if request.method == 'GET':
        bebida_buscada = request.GET['nombre']
        resultados_bebida = Bebida.objects.filter(nombre__icontains=bebida_buscada).order_by('nombre')
        
    return render(request, "AppWeb/buscarBebida.html", {'bebidas_b':resultados_bebida})

def buscarGuarnicion(request):
    return render(request, "AppWeb/buscarGuarnicion.html")

def resultadosGuarnicion(request):
    if request.method == 'GET':
        guarnicion_buscada = request.GET['nombre']
        resultados_guarnicion = Guarnicion.objects.filter(nombre__icontains=guarnicion_buscada).order_by('nombre')
        
    return render(request, "AppWeb/buscarGuarnicion.html", {'guarniciones_b':resultados_guarnicion})

def buscarPostre(request):
    return render(request, "AppWeb/buscarPostre.html")

def resultadosPostre(request):
    if request.method == 'GET':
        postre_buscado = request.GET['nombre']
        resultados_postre = Postre.objects.filter(nombre__icontains=postre_buscado).order_by('nombre')
        
    return render(request, "AppWeb/buscarPostre.html", {'postres_b':resultados_postre})

#Vistas para register, login, logout:

def login(request):

    if request.method == 'POST':

        formu = AuthenticationForm(request, data=request.POST)

        if formu.is_valid():
            info = formu.cleaned_data
            user = info['username']
            contra = info['password']
            usuario_actual = authenticate(username=user, password=contra)
            
            if usuario_actual is not None:
                login(request, usuario_actual)
                return render(request, "AppWeb/inicio.html", {'mensaje':f'Bienvenido, {usuario_actual}'})
        else:
            return render(request, "registro/login.html", {'mensaje':"Error, datos incorrectos."})
    else:
        formu = AuthenticationForm()
    return render(request, "registro/login.html", {'formu':formu})

def signup(request):

    if request.method == 'POST':

        formu = RegistrarUsuario(request.POST)

        if formu.is_valid():
            usuario = formu.save()
            login(request, usuario)
            return render(request, "AppWeb/inicio.html", {'mensaje':f'Bienvenido, {usuario}'})
        else:
            return render(request, "registro/signup.html", {'mensaje':"Error, datos incorrectos."})
    else:
        formu = RegistrarUsuario()
    return render(request, "registro/signup.html", {'formu':formu})

def logout(request):
    logout(request)
    return render(request, "AppWeb/inicio.html", {'mensaje':"Sesión cerrada."})