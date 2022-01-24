from django import forms


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
    
    