
from mailbox import NoSuchMailboxError
from django import forms

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class TrayectoFormulario(forms.Form):
    ruta=forms.CharField
    fechaSalida=forms.CharField
    fechaLlegada=forms.CharField
    
    def __str__(self):
        return f'{self.ruta} '
    
class OperadorFormulario(forms.Form):
    nombre=forms.CharField(max_length=10)
    direccion=forms.CharField(max_length=30)
    web=forms.CharField(max_length=20)
    telefono=forms.CharField(max_length=10)
    
    def __str__(self):
        return f'{self.nombre} {self.telefono}'

class ClienteFormulario(forms.Form):
    nombre=forms.CharField(max_length=10)
    email=forms.EmailField()
    telefono=forms.CharField(max_length=10)
    
    def __str__(self):
        return f'{self.nombre} {self.email}'