from re import template
from django.urls import path

from AppVuelos import views

from django.contrib.auth.views import LogoutView
from AppVuelos.views import inicio
urlpatterns = [
   
    path('', views.inicio, name="inicio"), 
    
    path('mantenimiento', views.mantenimiento, name="mantenimiento"), 
    
    # Operadores
    path('Operadores/', views.OperadoresList.as_view(), name='Operadores'),
    path('listaOperadores/', views.OperadorList.as_view(), name='List'),
    path('detalleOperadores/<pk>/', views.OperadorDetail.as_view(), name='Detail'),
    path('crearOperadores/', views.OperadorCreate.as_view(), name='New'),
    path('actualizaOperadores/<pk>/', views.OperadorUpdate.as_view(), name='Edit'),
    path('eliminaOperadores/<pk>/', views.OperadorDelete.as_view(), name='Delete'),
    
    # Trayectos
    path('Trayectos/', views.TrayectosList.as_view(), name='Trayectos'),
    path('listaTrayectos/', views.TrayectoList.as_view(), name='List_Trayectos'),
    path('detalleTrayectos/<pk>/', views.TrayectoDetail.as_view(), name='Detail_Trayectos'),
    path('crearTrayectos/', views.TrayectoCreate.as_view(), name='New_Trayectos'),
    path('actualizaTrayectos/<pk>/', views.TrayectoUpdate.as_view(), name='Edit_Trayectos'),
    path('eliminaTrayectos/<pk>/', views.TrayectoDelete.as_view(), name='Delete_Trayectos'),
    
    path('busquedaRuta/', views.busquedaRuta, name='busquedaRuta'),
    path('buscar/', views.buscar, name='buscar'),
    
    #Login
    path('login/', views.login_request, name='Login'),
    path('register/', views.register, name='Register'),
    
    #Logout
    path('logout/', LogoutView.as_view(template_name="AppVuelos/logout.html"), name='Logout'),
    
    #Editar Perfil
    path('editarPerfil/', views.editarPerfil, name='EditarPerfil'),
    
]