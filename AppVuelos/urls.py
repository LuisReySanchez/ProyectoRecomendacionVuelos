from django.urls import path

from AppVuelos import views

urlpatterns = [
   
    path('', views.inicio, name="inicio"), #esta era nuestra primer view
    
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
]