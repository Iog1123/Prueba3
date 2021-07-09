from rest_framework import serializers
from core.models import Proveedor


class ProveedorSerializer(serializers.ModelSerializer):

    class Meta:
        
        model = Proveedor
        fields = ['id_Proveedor','nombreCompleto', 'telefono', 'direccion','email','password','Pais']