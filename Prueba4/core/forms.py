
from django.forms import ModelForm
from .models import Pais,Proveedor
from django import forms




class ProveedorForm(ModelForm):
    
    class Meta:
        password = forms.CharField(widget=forms.PasswordInput())
        model = Proveedor
        fields = ['nombreCompleto', 'telefono', 'direccion','email','password','Pais']
        