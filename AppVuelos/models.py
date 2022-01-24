from django.db import models

# Create your models here.
class Operador(models.Model):
       
    nombre=models.CharField(max_length=40, null=True)
    direccion=models.CharField(max_length=40, null=True)
    web=models.CharField(max_length=40, null=True)
    telefono=models.CharField(max_length=12, null=True)


    def __str__(self):
        return self.nombre
    
    
class Trayecto(models.Model):
       
    ruta=models.CharField(max_length=10, null=True)
    fechaSalida=models.CharField(max_length=40, null=True)
    horaSalida=models.IntegerField()
    horaLlegada=models.IntegerField()


    def __str__(self):
        return f'{self.ruta} - {self.fechaSalida} - {self.horaSalida}'

# class Avion(models.Model):
       
#     modelo=models.CharField(max_length=10, null=True)
#     capacidad=models.IntegerField()
       