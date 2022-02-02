from django import forms

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

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
    
class UserEditForm(UserCreationForm):
    
    email=forms.EmailField(label="Modificar email")
    password1=forms.EmailField(label="Contraseña",widget=forms.PasswordInput)
    password2=forms.EmailField(label="Repetir la contraseña",widget=forms.PasswordInput)
    first_name=forms.CharField
    last_name=forms.CharField
    
    class Meta:
        model=User
        fields=['email','password1','password2','first_name','last_name']