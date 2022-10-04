from django.shortcuts import render

from cliente.models import Cliente
from turno.models import Turno



def myfirstview(request):
    data = {
        'name': 'Camila',
        'clientes': Cliente.objects.all()
    }

    return render(request, 'index.html', data)


def mysecondview(request):
    data = {
        'name': 'Camila',
        'turnos': Turno.objects.all()
    }

    return render(request, 'second.html', data)