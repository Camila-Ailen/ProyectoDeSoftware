from django.db import models


# Create your models here.
class Categoria(models.Model):
    nombre = models.CharField(max_length=100, default=None)

    def __str__(self):
        return self.nombre


class Ejercicio(models.Model):
    id_categoria = models.ManyToManyField(Categoria, default=None)
    nombre = models.CharField(max_length=100, null=False, default=None)
    detalle = models.CharField(max_length=100, null=False, default=None)

    def __str__(self):
        return self.nombre


class Rutina(models.Model):
    id_ejercicio = models.ForeignKey(Ejercicio, on_delete=models.CASCADE, default=None)
    id_categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE, default=None)
    cantidadMax = models.IntegerField(default=10)
    cantidadMin = models.IntegerField(default=2)
