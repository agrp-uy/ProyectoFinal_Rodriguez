from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.models import User
from AppWeb.models import Comida, Bebida, Guarnicion, Postre

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

class RegistrarUsuario(UserCreationForm):
    nombre = forms.CharField(label='Nombre', max_length=50)
    apellido = forms.CharField(label='Apellido', max_length=50)
    direccion = forms.CharField(label='Direccion', max_length=100)
    telefono = forms.IntegerField(label='Telefono')
    email = forms.EmailField(label='Email', max_length=50)
    password1 = forms.CharField(label='Contraseña', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Confirmar contraseña', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'password1', 'password2', 'nombre', 'apellido', 'direccion', 'telefono', 'email']