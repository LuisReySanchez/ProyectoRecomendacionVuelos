from dataclasses import fields
from django.shortcuts import render

from AppVuelos.forms import TrayectoFormulario
from AppVuelos.models import Operador, Trayecto

from django.views.generic import ListView

from django.views.generic.detail import DetailView

from django.views.generic.edit import CreateView, UpdateView, DeleteView

def inicio(request):
    return render(request,"AppVuelos/inicio.html")

# def trayectos(request):
#     return render(request,"AppVuelos/trayectos.html")

#######################################################################################################
#TRAYECTO
#######################################################################################################

def leer_trayectos(request):
      
      trayectos=Trayecto.objects.all()
      
      return render(request,"AppVuelos/lista_trayectos.html",{"trayectos":trayectos})

def trayectos(request):
    
      if(request.method == 'POST'):

            mi_formulario = TrayectoFormulario(request.POST)

            if mi_formulario.is_valid():

                  data = mi_formulario.cleaned_data

                  trayecto = Trayecto(ruta=data["ruta"], fechaSalida=data["fechaSalida"], fechaLlegada=data["fechaLlegada"])

                  trayecto.save()

                  return render(request, "AppVuelos/inicio.html")
      
      else:

            mi_formulario = TrayectoFormulario()

      return render(request, "AppVuelos/trayectos.html", {"form": mi_formulario})


def elimina_trayecto(request, id_trayecto):
    
      trayecto = Trayecto.objects.get(id=id_trayecto)

      trayecto.delete()

      trayecto = Trayecto.objects.all()

      return render(request, "AppVuelos/lista_trayectos.html", {"trayectos": trayectos})


def editarTrayecto(request, trayecto_ruta):
    
      #Recibe el nombre del profesor que vamos a modificar
      trayecto = Trayecto.objects.get(ruta=trayecto_ruta)

      #Si es metodo POST hago lo mismo que el agregar
      if request.method == 'POST':

            miFormulario = TrayectoFormulario(request.POST) #aquí mellega toda la información del html

            
            if miFormulario.is_valid:   #Si pasó la validación de Django

                  informacion = miFormulario.cleaned_data

                  trayecto.ruta = informacion['ruta']
                  trayecto.fechaSalida = informacion['fechaSalida']
                  trayecto.fechaLlegada = informacion['fechaLlegada']
                  trayecto.save()

                  return render(request, "AppVuelos/inicio.html") #Vuelvo al inicio o a donde quieran
      #En caso que no sea post
      else: 
            #Creo el formulario con los datos que voy a modificar
            miFormulario= TrayectoFormulario(initial={'ruta': trayecto.ruta, 'fechaSalida':trayecto.fechaSalida , 
            'fechaLlegada':trayecto.fechaLlegada}) 

      #Voy al html que me permite editar
      return render(request, "AppVuelos/editarTrayecto.html", {"miFormulario":miFormulario, "trayecto_ruta":trayecto_ruta})



#######################################################################################################
# OPERADOR
#######################################################################################################

def operador(request):
    lista=Operador.objects.all()
    
    return render(request,"AppVuelos/operador.html", {"lista":lista})


class OperadorList(ListView):
    
      model = Operador
      template_name = "AppVuelos/operador_list.html"

class OperadorDetail(DetailView):

      model = Operador
      template_name = "AppVuelos/operador_detail.html"

class OperadorUpdate(UpdateView):

      model = Operador
      success_url = '/AppVuelos/listaOperador'
      fields = ['nombre', 'direccion','web','telefono']

class OperadorDelete(DeleteView):

      model = Operador
      success_url = '/AppVuelos/listaCursos'
      template_name = 'AppVuelos/operador_confirm_delete.html'

class OperadorCreate(CreateView):

      model = Operador
      fields = ['nombre', 'direccion','web','telefono']
      success_url = '/AppVuelos/listaOperadores'



#######################################################################################################
# CLIENTE
#######################################################################################################

def cliente(request):
    return render(request,"AppVuelos/cliente.html")

