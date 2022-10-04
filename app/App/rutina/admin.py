from django.contrib import admin
from rutina.models import *
from cliente.models import *
from pago.models import *
from turno.models import *

# Register your models here.
admin.site.register(Ejercicio)
admin.site.register(Cliente)
admin.site.register(Mes)
admin.site.register(Categoria)
admin.site.register(Rutina)