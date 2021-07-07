
from django.forms import ModelForm
from .models import Pais,Proveedor
from django import forms




class ProveedorForm(ModelForm):
    password = forms.CharField(widget=forms.PasswordInput(render_value=True))
    class Meta:
        
        model = Proveedor
        fields = ['nombreCompleto', 'telefono', 'direccion','email','password','Pais']
        