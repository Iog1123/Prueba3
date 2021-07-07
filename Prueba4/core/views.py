from core.models import Proveedor
from core.forms import ProveedorForm
from django.shortcuts import redirect, render


# Create your views here.

def index(request):
    return render(request,'core/index.html')

def tabla1(request):
    return render(request,'core/tabla1.html')

def tabla2(request):
    return render(request,'core/tabla2.html')

def tabla3(request):
    return render(request,'core/tabla3.html')

def somos(request):
    return render(request,'core/somos.html')

def contacto(request):
    return render(request,'core/contacto.html')



     

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



def form_mod_proveedor(request, id):

    proveedor = Proveedor.objects.get(id_Proveedor=id)

    datos = {
        'form' : ProveedorForm(instance=proveedor)
    }

    if request.method == 'POST':
        formulario = ProveedorForm(request.POST, instance=proveedor)
        if formulario.is_valid:
            formulario.save()
            datos['form'] = formulario
            datos['mensaje'] = "Proveedor Modificado correctamente"

    return render(request, 'core/form_mod_proveedor.html', datos)


def form_del_proveedor(request, id):

    proveedor = Proveedor.objects.get(id_Proveedor=id)

    proveedor.delete()
    mensaje = "Proveedor Eliminado"
    
    return redirect(to="proveedor")