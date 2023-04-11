from django.db import models

# Create your models here.

class t_cuerpo (models.Model):

    cuerpo = models.CharField(max_length=200)

    def __str__ (self):
        return self.nombre



class t_ejercicio (models.Model):

    cuerpo = models.ForeignKey(t_cuerpo,on_delete=models.CASCADE)
    ejercicio = models.CharField(max_length=200)
    posicion = models.CharField(max_length=200)
    tipo = models.CharField(max_length=200)
    repeticiones = models.IntegerField()

    def __str__ (self):
        return self.nombre
