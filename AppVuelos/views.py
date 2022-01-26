from dataclasses import fields
from django.shortcuts import render, HttpResponse

from AppVuelos.forms import OperadorFormulario,TrayectoFormulario

from AppVuelos.models import Operador, Trayecto


from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import UpdateView, DeleteView, CreateView

from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout, authenticate

from django.contrib.auth.forms import UserCreationForm

#Mixin
from django.contrib.auth.mixins import LoginRequiredMixin

#Decoradores
from django.contrib.auth.decorators import login_required

# Inicio
############################################################################

def inicio(request):

      return render(request, "AppVuelos/inicio.html")

############################################################################
# OPERADOR
############################################################################

# Listado de Operadores + Mixin
class OperadoresList(LoginRequiredMixin,ListView):
    
      model = Operador
      template_name = "AppVuelos/operadores.html"

# CRUD Operadores
class OperadorList(ListView):

      model = Operador
      template_name = "AppVuelos/operador_list.html"

class OperadorDetail(DetailView):

      model = Operador
      template_name = "AppVuelos/operador_detail.html"

class OperadorUpdate(UpdateView):

      model = Operador
      success_url = '/listaOperadores'
      fields = ['nombre', 'direccion','web','telefono']

class OperadorDelete(DeleteView):

      model = Operador
      success_url = '/listaOperadores'
      template_name = 'AppVuelos/operador_confirm_delete.html'

class OperadorCreate(CreateView):

      model = Operador
      fields = ['nombre', 'direccion','web','telefono']
      success_url = '/listaOperadores' 






############################################################################
# TRAYECTO
############################################################################

# Listado de Trayectos
class TrayectosList(ListView):
    
      model = Trayecto
      template_name = "AppVuelos/trayectos.html"

# CRUD Trayectos
class TrayectoList(ListView):

      model = Trayecto
      template_name = "AppVuelos/trayecto_list.html"

class TrayectoDetail(DetailView):

      model = Trayecto
      template_name = "AppVuelos/trayecto_detail.html"

class TrayectoUpdate(UpdateView):

      model = Trayecto
      success_url = '/listaTrayectos'
      fields = ['ruta', 'fechaSalida','horaSalida','horaLlegada']

class TrayectoDelete(DeleteView):

      model = Trayecto
      success_url = '/listaTrayectos'
      template_name = 'AppVuelos/trayecto_confirm_delete.html'

class TrayectoCreate(CreateView):

      model = Trayecto
      fields = ['ruta', 'fechaSalida','horaSalida','horaLlegada']
      success_url = '/listaTrayectos' 

# Busqueda de Fechas de Salida para una Ruta
############################################################################

# View de Busqueda con autenticacion correcta
@login_required
def busquedaRuta(request):
      return render(request,"AppVuelos/busquedaRuta.html")

# Resultado de la Busqueda
def buscar(request):
      
      if (request.method=='GET'):
            
            ruta=request.GET['ruta']
            fechaSalida=Trayecto.objects.filter(ruta=ruta)
      
            return render(request,"AppVuelos/resultadosBusqueda.html",{'fechaSalida':fechaSalida})
      else:
            return HttpResponse('No enviaste datos')


############################################################################
# LOGIN
############################################################################

# Autenticacion
############################################################################

def login_request(request):
      
      if (request.method =="POST"):
            
            form=AuthenticationForm(request, data=request.POST)
            
            if form.is_valid():
                 
                 data=form.cleaned_data
                 
                 user=authenticate(username=data['username'],password=data['password'])
                 
                 if user is not None:
                       
                       login(request,user)
                        
                       return render(request,"AppVuelos/inicio.html",{'mensaje':f'Bienvenido {user.get_username()}'})
      
                 else:
                       return render(request,"AppVuelos/inicio.html",{'mensaje':'Fallo la autenticacion intentalo otra vez'})
                 
            else:
                
                return render(request,"AppVuelos/inicio.html",{'mensaje':'Formulario erroneo'})
      
      else:
            form=AuthenticationForm()
            
            return render(request,"AppVuelos/login.html",{'form':form})
      
# Regitro
############################################################################

def register(request):
      if request.method=="POST":
            form=UserCreationForm(request.POST)
            if form.is_valid():
                  username=form.cleaned_data['username']
                  
                  form.save()
                  return render(request,"AppVuelos/inicio.html",{"mensaje":"Usuario creado con exito"})
      
            else:
                  return render(request,"AppVuelos/inicio.html",{"mensaje":"Usuario no creado"})
                   
                  
      else:
            # formulario de creacion de instancia
            form= UserCreationForm()
            
            return render(request,"AppVuelos/registro.html",{"form":form})     
      
    