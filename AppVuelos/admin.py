from django.contrib import admin

from AppVuelos.models import Trayecto,Operador, Cliente


# Register your models here.
admin.site.register(Trayecto)
admin.site.register(Operador)
admin.site.register(Cliente)

