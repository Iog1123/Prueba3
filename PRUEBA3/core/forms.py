from django.forms import ModelForm
from .models import Pais,Proveedor

class ProveedorForm(ModelForm):

    
    class Meta:
        model = Proveedor
        fields = ['id_Proveedor', 'nombreCompleto', 'telefono', 'direccion','email','password','Pais']