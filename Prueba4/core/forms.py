
from django.forms import ModelForm
from .models import Pais,Proveedor
from django import forms




class ProveedorForm(ModelForm):
    
    class Meta:
        password = forms.CharField(widget=forms.PasswordInput())
        model = Proveedor
        fields = ['id_Proveedor', 'nombreCompleto', 'telefono', 'direccion','email','password','Pais']
        