# Generated by Django 4.1.1 on 2022-10-03 06:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pago', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='pago',
            name='fechaYHora',
            field=models.DateTimeField(auto_now_add=True, null=True, verbose_name='Fecha y Hora'),
        ),
        migrations.AddField(
            model_name='pago',
            name='id_mes',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='pago.mes'),
        ),
        migrations.AddField(
            model_name='pago',
            name='id_tipoPago',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='pago.tipopago'),
        ),
        migrations.AddField(
            model_name='pago',
            name='montoDePago',
            field=models.DecimalField(decimal_places=2, max_digits=6, null=True, verbose_name='Monto de Pago'),
        ),
        migrations.AddField(
            model_name='pago',
            name='nroComprobante',
            field=models.IntegerField(null=True, verbose_name='Numero de Comprobante'),
        ),
    ]
