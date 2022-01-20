from django.db import models

class Trayecto(models.Model):
    ruta=models.CharField
    fechaSalida=models.CharField
    fechaLlegada=models.CharField
    
    def __str__(self):
        return f'{self.ruta} '
    
class Operador(models.Model):
    nombre=models.CharField(max_length=10)
    direccion=models.CharField(max_length=30)
    web=models.CharField(max_length=20)
    telefono=models.CharField(max_length=10)
    
    def __str__(self):
        return f'{self.nombre}'

class Cliente(models.Model):
    nombre=models.CharField(max_length=10)
    email=models.EmailField()
    telefono=models.CharField(max_length=10)
    
    def __str__(self):
        return f'{self.nombre} {self.email}'




    
