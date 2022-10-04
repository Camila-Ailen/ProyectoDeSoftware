from datetime import date

from django.db import models


# Create your models here.
# -------------------------CLIENTE----------------------------------------------------------------
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


# -------------------------PAGO---------------------------------------------------------------------
class TipoPago(models.Model):
    detalle = models.CharField(max_length=100),

    def __str__(self):
        return self.detalle


class Mes(models.Model):
    detalle = models.CharField(max_length=20, default=None)

    def __str__(self):
        return self.detalle


class Pago(models.Model):
    id_cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    id_mes = models.ForeignKey(Mes, on_delete=models.CASCADE, default=None)
    id_tipoPago = models.ForeignKey(TipoPago, on_delete=models.CASCADE, default=None)
    fechaYHora = models.DateTimeField(auto_now_add=True, null=True, verbose_name='Fecha y Hora')
    montoDePago = models.DecimalField(max_digits=6, decimal_places=2, null=True, verbose_name='Monto de Pago')
    nroComprobante = models.IntegerField(null=True, verbose_name='Numero de Comprobante')
    detalle = models.CharField(max_length=100, verbose_name='Detalle', default=None)

    def __str__(self):
        return self.nroComprobante


# -------------------------RUTINA-------------------------------------------------------------------
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


# -------------------------TURNO---------------------------------------------------------------------------
class Turno(models.Model):
    id_cliente = models.ManyToManyField(Cliente),
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
    id_cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE, default=None)
    fechaHoy = models.DateField(default=date.today)

    def __str__(self):
        return self.fechaHoy

    class Meta:
        verbose_name = 'TurnoTemporal'
        verbose_name_plural = 'TurnosTemporales'
        db_table = 'turnoTemporal'


# -------------------------ASISTENCIA-----------------------------------------------------------------------
class Asistencia(models.Model):
    id_turno = models.ForeignKey(Turno, on_delete=models.CASCADE)
    id_cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    fechaYHora = models.DateTimeField(auto_now_add=True)
