from django.contrib import admin
import AppVuelos

from AppVuelos.models import Operador, Trayecto

admin.site.register(Operador)
admin.site.register(Trayecto)