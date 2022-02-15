from cProfile import label
import email
from logging import PlaceHolder
from tkinter import HIDDEN
from unicodedata import name
from django import forms

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from sqlalchemy import false

class OperadorFormulario(forms.Form):

    #Especificar los campos
    nombre = forms.CharField()
    direccion = forms.CharField()
    web = forms.CharField()
    telefono = forms.CharField()


class TrayectoFormulario(forms.Form):
    
    #Especificar los campos
    ruta = forms.CharField()
    fechaSalida = forms.CharField()
    horaSalida = forms.IntegerField
    horaLlegada = forms.IntegerField()  


class UserRegisterForm(UserCreationForm):
    username=forms.CharField(label=False,widget= forms.TextInput(attrs={'placeholder':'Ingrese usuario'}))
    email=forms.EmailField(label=False,widget= forms.TextInput(attrs={'placeholder':'Ingrese su Email'}))

    password1=forms.CharField(label=False,widget=forms.PasswordInput(attrs={'placeholder':'Ingrese su constraseña'}))
    password2=forms.CharField(label=False,widget=forms.PasswordInput(attrs={'placeholder':'Repetir contraseña'}))
    
    first_name=forms.CharField(label=False,widget= forms.TextInput(attrs={'placeholder':'Ingrese nombre'}))
    last_name=forms.CharField(label=False,widget= forms.TextInput(attrs={'placeholder':'Ingrese apellidos'}))
    
    class Meta:
        model=User
        fields=['username','email','password1','password2','first_name','last_name']
          
        
class UserEditForm(UserCreationForm):
    
    email=forms.EmailField(label="Modificar email")
    password1=forms.CharField(label="Contraseña",widget=forms.PasswordInput)
    password2=forms.CharField(label="Repetir la contraseña",widget=forms.PasswordInput)
    first_name=forms.CharField()
    last_name=forms.CharField()

    
    class Meta:
        model=User
        fields=['email','password1','password2','first_name','last_name']
        
        
class ContactoForm(forms.Form):
    nombre=forms.CharField(label="Nombre",required=True)
    email=forms.CharField(label="Email",required=True)
    
    contenido=forms.CharField(label="Contenido", widget=forms.Textarea)    
