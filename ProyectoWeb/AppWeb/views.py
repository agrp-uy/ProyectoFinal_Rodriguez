from AppWeb.models import *
from AppWeb.forms import *
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, TemplateView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.shortcuts import render
from django.contrib.auth.decorators import user_passes_test
from django.utils.decorators import method_decorator


#Vistas generales:

class InicioView(TemplateView):
    template_name = "AppWeb/inicio.html"

class CartaView(LoginRequiredMixin, TemplateView):
    template_name = "AppWeb/carta.html"

class PedidoView(LoginRequiredMixin, TemplateView):
    template_name = "AppWeb/pedido.html"

class AboutView(TemplateView):
    template_name = "AppWeb/about.html"


#Vistas para login, logout y signup de usuarios:

def user_login(request):
    if request.method == 'POST':
        formu = AuthenticationForm(request, data=request.POST)

        if formu.is_valid():
            info = formu.cleaned_data
            user = info['username']
            contra = info['password']
            usuario_actual = authenticate(username=user, password=contra)
            
            if usuario_actual is not None:
                login(request, usuario_actual)
                return render(request, "AppWeb/inicio.html", {'mensaje':f'Bienvenido, {usuario_actual.first_name}'})
            else:
                return render(request, "registro/login.html", {'formu': formu, 'mensaje':"Error, datos incorrectos."})
        else:
            return render(request, "registro/login.html", {'formu': formu, 'mensaje':"Error, datos incorrectos."})
    else:
        formu = AuthenticationForm()
    return render(request, "registro/login.html", {'formu':formu})

def user_signup(request):
    if request.method == 'POST':
        formu = RegistrarUsuario(request.POST)
        if formu.is_valid():
            user = formu.save()
            login(request, user)
            return render(request, "AppWeb/inicio.html", {'mensaje':f'Bienvenido, {user.first_name}'})
    else:
        formu = RegistrarUsuario()
    return render(request, "registro/signup.html", {'formu':formu})

def user_logout(request):
    logout(request)
    return render(request, "registro/logout.html", {'mensaje':"Sesión cerrada."})


#Vistas varias:

def es_staff(user): #Función para validar al usuario como staff
    return user.is_staff

def acceso_denegado(request): #Vista para cuando el usuario no tiene permisos de staff
    return render(request, "AppWeb/errores/accesoDenegado.html", {'mensaje': 'No cuenta con los privilegios para realizar esa acción'})

def en_construccion(request): #Vista para las secciones que aún no están listas
    return render(request, 'AppWeb/errores/enConstruccion.html')


#vistas para crear objetos de cada modelo (C)

@method_decorator(user_passes_test(es_staff, login_url='accesoDenegado'), name='dispatch')  
class AgregarComida(LoginRequiredMixin, CreateView):
    model = Comida
    form_class = ComidaForm
    template_name = "AppWeb/Comida/agregarComida.html"
    success_url = reverse_lazy('inicio')

@method_decorator(user_passes_test(es_staff, login_url='accesoDenegado'), name='dispatch')  
class AgregarBebida(LoginRequiredMixin, CreateView):
    model = Bebida
    form_class = BebidaForm
    template_name = "AppWeb/Bebida/agregarBebida.html"
    success_url = reverse_lazy('inicio')

@method_decorator(user_passes_test(es_staff, login_url='accesoDenegado'), name='dispatch')  
class AgregarGuarnicion(LoginRequiredMixin, CreateView):
    model = Guarnicion
    form_class = GuarnicionForm
    template_name = "AppWeb/Guarnicion/agregarGuarnicion.html"
    success_url = reverse_lazy('inicio')

@method_decorator(user_passes_test(es_staff, login_url='accesoDenegado'), name='dispatch')  
class AgregarPostre(LoginRequiredMixin, CreateView):
    model = Postre
    form_class = PostreForm
    template_name = "AppWeb/Postre/agregarPostre.html"
    success_url = reverse_lazy('inicio')


#Vistas para leer los objetos de cada modelo (R)

class ComidaView(LoginRequiredMixin, ListView):
    model = Comida
    template_name = "AppWeb/Comida/comida.html"
    context_object_name = 'comidas'
    ordering = ['nombre']

class BebidaView(LoginRequiredMixin, ListView):
    model = Bebida
    template_name = "AppWeb/Bebida/bebida.html"
    context_object_name = 'bebidas'
    ordering = ['nombre']

class GuarnicionView(LoginRequiredMixin, ListView):
    model = Guarnicion
    template_name = "AppWeb/Guarnicion/guarnicion.html"
    context_object_name = 'guarniciones'
    ordering = ['nombre']

class PostreView(LoginRequiredMixin, ListView):
    model = Postre
    template_name = "AppWeb/Postre/postre.html"
    context_object_name = 'postres'
    ordering = ['nombre']


#Vistas para editar los objetos de cada modelo (U)

@method_decorator(user_passes_test(es_staff, login_url='accesoDenegado'), name='dispatch')  
class ActualizarComida(LoginRequiredMixin, UpdateView):
    model = Comida
    form_class = ComidaForm
    template_name = 'AppWeb/Comida/actualizarComida.html'
    success_url = '/comida/'

@method_decorator(user_passes_test(es_staff, login_url='accesoDenegado'), name='dispatch')  
class ActualizarBebida(LoginRequiredMixin, UpdateView):
    model = Bebida
    form_class = BebidaForm
    template_name = 'AppWeb/Bebida/actualizarBebida.html'
    success_url = '/bebida/'

@method_decorator(user_passes_test(es_staff, login_url='accesoDenegado'), name='dispatch')  
class ActualizarGuarnicion(LoginRequiredMixin, UpdateView):
    model = Guarnicion
    form_class = GuarnicionForm
    template_name = 'AppWeb/Guarnicion/actualizarGuarnicion.html'
    success_url = '/guarnicion/'

@method_decorator(user_passes_test(es_staff, login_url='accesoDenegado'), name='dispatch')  
class ActualizarPostre(LoginRequiredMixin, UpdateView):
    model = Postre
    form_class = PostreForm
    template_name = 'AppWeb/Postre/actualizarPostre.html'
    success_url = '/postre/'


#Vistas para eliminar los objetos de cada modelo (D)

@method_decorator(user_passes_test(es_staff, login_url='accesoDenegado'), name='dispatch')  
class EliminarComida(LoginRequiredMixin, DeleteView):
    model = Comida
    template_name = 'AppWeb/Comida/eliminarComida.html'
    success_url = '/comida/'

@method_decorator(user_passes_test(es_staff, login_url='accesoDenegado'), name='dispatch')  
class EliminarBebida(LoginRequiredMixin, DeleteView):
    model = Bebida
    template_name = 'AppWeb/Bebida/eliminarBebida.html'
    success_url = '/bebida/'

@method_decorator(user_passes_test(es_staff, login_url='accesoDenegado'), name='dispatch')  
class EliminarGuarnicion(LoginRequiredMixin, DeleteView):
    model = Guarnicion
    template_name = 'AppWeb/Guarnicion/eliminarGuarnicion.html'
    success_url = '/guarnicion/'

@method_decorator(user_passes_test(es_staff, login_url='accesoDenegado'), name='dispatch')  
class EliminarPostre(LoginRequiredMixin, DeleteView):
    model = Postre
    template_name = 'AppWeb/Postre/eliminarPostre.html'
    success_url = '/postre/'


#Vistas para los formularios de busqueda:

@login_required
def buscarComida(request):
    return render(request, "AppWeb/Comida/buscarComida.html")

@login_required
def buscarBebida(request):
    return render(request, "AppWeb/Bebida/buscarBebida.html")

@login_required
def buscarGuarnicion(request):
    return render(request, "AppWeb/Guarnicion/buscarGuarnicion.html")

@login_required
def buscarPostre(request):
    return render(request, "AppWeb/Postre/buscarPostre.html")


#Vistas para los resultados de busqueda:
#Se aplica filtro para buscar por nombre (o letras) y el resultado se ordena alfabeticamente

@login_required
def resultadosComida(request):
    if request.method == 'GET':
        comida_buscada = request.GET['nombre']
        resultados_comida = Comida.objects.filter(nombre__icontains=comida_buscada).order_by('nombre')
        
    return render(request, "AppWeb/Comida/buscarComida.html", {'comidas_b':resultados_comida})

@login_required
def resultadosBebida(request):
    if request.method == 'GET':
        bebida_buscada = request.GET['nombre']
        resultados_bebida = Bebida.objects.filter(nombre__icontains=bebida_buscada).order_by('nombre')
        
    return render(request, "AppWeb/Bebida/buscarBebida.html", {'bebidas_b':resultados_bebida})

@login_required
def resultadosGuarnicion(request):
    if request.method == 'GET':
        guarnicion_buscada = request.GET['nombre']
        resultados_guarnicion = Guarnicion.objects.filter(nombre__icontains=guarnicion_buscada).order_by('nombre')
        
    return render(request, "AppWeb/Guarnicion/buscarGuarnicion.html", {'guarniciones_b':resultados_guarnicion})

@login_required
def resultadosPostre(request):
    if request.method == 'GET':
        postre_buscado = request.GET['nombre']
        resultados_postre = Postre.objects.filter(nombre__icontains=postre_buscado).order_by('nombre')
        
    return render(request, "AppWeb/Postre/buscarPostre.html", {'postres_b':resultados_postre})


#Vistas para editar perfil de usuario:

@login_required
def editar_perfil(request):
    usuario = request.user
    if request.method == 'POST':
        formu = FormularioEditar(request.POST)
        if formu.is_valid():
            info = formu.cleaned_data
            usuario.set_password(info['password1'])
            usuario.first_name = info['first_name']
            usuario.last_name = info['last_name']
            usuario.email = info['email']
            usuario.save()
            user = authenticate(username=usuario.username, password=info['password1']) #Se aplica el authenticate para que el usuario no tenga que volver a iniciar sesión
            if user is not None:
                login(request, user)
        
            return render(request, "AppWeb/inicio.html", {'mensaje':f'Se actualizaron tus datos, {usuario.first_name}'})
    else:
        formu = FormularioEditar(
            initial={
                'first_name': usuario.first_name,
                'last_name': usuario.last_name,
                'email': usuario.email,
            })
    return render(request, "registro/editarPerfil.html", {'formu':formu})

@login_required
def agregar_avatar(request):
    if request.method == 'POST':
        formu = FormularioAvatar(request.POST, request.FILES)
        if formu.is_valid():
            usuario_actual = User.objects.get(username=request.user)
            avatar = Avatar(usuario=usuario_actual, imagen=formu.cleaned_data['imagen'])
            avatar.save()
            return render(request, "AppWeb/inicio.html", {'mensaje':f'Avatar agregado.'})
    else:
        formu = FormularioAvatar()

    return render(request, "registro/agregarAvatar.html", {'formu':formu})

