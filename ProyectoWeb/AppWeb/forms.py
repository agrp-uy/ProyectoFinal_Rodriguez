from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from AppWeb.models import *


#Formularios para los modelos de Productos:

class ComidaForm(forms.ModelForm):
    class Meta:
        model = Comida
        fields = ['nombre', 'descripcion', 'precio']

class BebidaForm(forms.ModelForm):
    class Meta:
        model = Bebida
        fields = ['nombre', 'descripcion', 'precio']

class GuarnicionForm(forms.ModelForm):
    class Meta:
        model = Guarnicion
        fields = ['nombre', 'descripcion', 'precio']

class PostreForm(forms.ModelForm):
    class Meta:
        model = Postre
        fields = ['nombre', 'descripcion', 'precio']


#Formularios para usuarios:
        
class RegistrarUsuario(UserCreationForm):
    password1 = forms.CharField(label='Contraseña', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Confirmar contraseña', widget=forms.PasswordInput)
    email = forms.EmailField(label='Email', max_length=50)

    class Meta:
        model = User
        fields = ['username', 'password1', 'password2', "first_name", "last_name", 'email']

class FormularioEditar(UserCreationForm):
    password1 = forms.CharField(label='Contraseña', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Confirmar contraseña', widget=forms.PasswordInput)
    email = forms.EmailField(label='Email', max_length=50)

    class Meta:
        model = User
        fields = ['password1', 'password2', "first_name", "last_name", 'email']

class FormularioAvatar(forms.ModelForm):
    class Meta:
        model = Avatar
        fields = ['imagen']