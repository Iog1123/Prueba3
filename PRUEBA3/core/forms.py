from django.forms import ModelForm
from .models import Pais,Proveedor
from django import forms

class ProveedorForm(ModelForm):
    class Meta:
        model = Proveedor
        fields = ['id_Proveedor', 'nombreCompleto', 'telefono', 'direccion','email','password','Pais']
        widgets = {
        'password': forms.PasswordInput()
    }