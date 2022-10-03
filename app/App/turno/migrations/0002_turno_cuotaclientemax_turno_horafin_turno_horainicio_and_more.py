# Generated by Django 4.1.1 on 2022-10-03 06:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('turno', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='turno',
            name='cuotaClienteMax',
            field=models.IntegerField(default=0, null=True, verbose_name='Cuota maxima de clientes'),
        ),
        migrations.AddField(
            model_name='turno',
            name='horaFin',
            field=models.TimeField(default=None, verbose_name='Hora de fin'),
        ),
        migrations.AddField(
            model_name='turno',
            name='horaInicio',
            field=models.TimeField(default=None, verbose_name='Hora de inicio'),
        ),
        migrations.AddField(
            model_name='turno',
            name='precio',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=7, verbose_name='Precio'),
        ),
    ]