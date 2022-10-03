from django.db import models


# Create your models here.

class Cliente(models.Model):
    nombre = models.CharField(max_length=100, verbose_name='Nombre', default=None)
    apellido = models.CharField(max_length=100, verbose_name='Apellido', default=None)
    dni = models.CharField(max_length=8, verbose_name='Dni', default=None),
    numTelefono = models.CharField(max_length=30, verbose_name='Numero de telefono', default=None)
    email = models.CharField(max_length=100, verbose_name='Email', default=None, null=True)
    estado = models.BooleanField(default=True, verbose_name='Estado')
    estaEnDeuda = models.BooleanField(default=False, verbose_name='Deuda')
    avatar = models.ImageField(upload_to='avatar', null=True, blank=True)

    def __str__(self):
        return self.apellido, self.nombre

    class Meta:
        verbose_name = 'Cliente'
        verbose_name_plural = 'Clientes'
        db_table = 'cliente'
