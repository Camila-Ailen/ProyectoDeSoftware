# Generated by Django 4.1.1 on 2022-10-03 05:59

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Turno',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cuotaClienteMin', models.IntegerField(default=0, null=True, verbose_name='Cuota minima de clientes')),
            ],
            options={
                'verbose_name': 'Turno',
                'verbose_name_plural': 'Turnos',
                'db_table': 'turno',
            },
        ),
        migrations.CreateModel(
            name='TurnoTemporal',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fechaHoy', models.DateField(default=datetime.date.today)),
                ('id_turno', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='turno.turno')),
            ],
            options={
                'verbose_name': 'TurnoTemporal',
                'verbose_name_plural': 'TurnosTemporales',
                'db_table': 'turnoTemporal',
            },
        ),
    ]
