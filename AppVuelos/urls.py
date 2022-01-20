from django.contrib.auth.views import LogoutView

from django.urls import path
from AppVuelos import views

urlpatterns = [
    path('', views.inicio,name='Inicio'),
    
    path('trayectos/', views.trayectos, name="Trayectos"),
    path('lista_trayectos/', views.leer_trayectos, name="lista_trayectos"),
    path('eliminarTrayecto/', views.elimina_trayecto, name="EliminarTrayecto"),
    path('editarTrayecto/', views.editarTrayecto, name="EditarTrayecto"),
    path('agregarTrayecto/', views.trayectos, name="AgregaTrayecto"),
    
    
    
    path('operador/', views.operador, name="Operador"),
    path('cliente/', views.cliente, name="Cliente"),
    
    path('listaOperadores/', views.OperadorList.as_view(), name='List'),
    path('crearOperador/', views.OperadorCreate.as_view(), name="New"),
   
    
    ]


