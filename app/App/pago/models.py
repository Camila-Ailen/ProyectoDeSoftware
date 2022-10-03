from django.db import models
# from App.cliente.models import Cliente


# Create your models here.
class TipoPago(models.Model):
    detalle = models.CharField(max_length=100),

    def __str__(self):
        return self.detalle


class Mes(models.Model):
    detalle = models.CharField(max_length=20),

    def __str__(self):
        return self.detalle


class Pago(models.Model):
#    id_cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    id_mes = models.ForeignKey(Mes, on_delete=models.CASCADE, default=None)
    id_tipoPago = models.ForeignKey(TipoPago, on_delete=models.CASCADE, default=None)
    fechaYHora = models.DateTimeField(auto_now_add=True, null=True, verbose_name='Fecha y Hora')
    montoDePago = models.DecimalField(max_digits=6, decimal_places=2, null=True, verbose_name='Monto de Pago')
    nroComprobante = models.IntegerField(null=True, verbose_name='Numero de Comprobante')
    detalle = models.CharField(max_length=100, verbose_name='Detalle', default=None)

    def __str__(self):
        return self.nroComprobante
