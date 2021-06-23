from core.models import Proveedor
from core.forms import ProveedorForm
from django.shortcuts import render


# Create your views here.

def index(request):

    return render(request,'core/index.html')

     

def form_datos(request):

    return render(request,'core/form_datos.html')

def proveedor(request):
    proveedor = Proveedor.objects.all()
    datos = {
        "proveedor" : proveedor
    }
    return render(request,'core/proveedor.html',datos)


def form_datos(request):
    datos = {
        'form' : ProveedorForm()
    }

    if request.method == 'POST':
        formulario = ProveedorForm(request.POST)
        if formulario.is_valid:
            formulario.save()
            datos['mensaje'] = "Datos Guardados correctamente"

    return render(request, 'core/form_datos.html', datos)