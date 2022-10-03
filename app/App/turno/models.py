from django.db import models
# from App.cliente.models import Cliente
from datetime import date


# Create your models here.
class Turno(models.Model):
#   id_cliente = models.ManyToManyField(Cliente),
    horaInicio = models.TimeField(default=None, verbose_name='Hora de inicio')
    horaFin = models.TimeField(default=None, verbose_name='Hora de fin')
    precio = models.DecimalField(max_digits=7, decimal_places=2, default=0.00, verbose_name='Precio')
    cuotaClienteMax = models.IntegerField(default=0, null=True, verbose_name='Cuota maxima de clientes')
    cuotaClienteMin = models.IntegerField(default=0, null=True, verbose_name='Cuota minima de clientes')

    def __str__(self):
        return self.horaInicio

    class Meta:
        verbose_name = 'Turno'
        verbose_name_plural = 'Turnos'
        db_table = 'turno'


class TurnoTemporal(models.Model):
    id_turno = models.ForeignKey(Turno, on_delete=models.CASCADE, default=None)
#    id_cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE, default=None)
    fechaHoy = models.DateField(default=date.today)

    def __str__(self):
        return self.fechaHoy

    class Meta:
        verbose_name = 'TurnoTemporal'
        verbose_name_plural = 'TurnosTemporales'
        db_table = 'turnoTemporal'
