from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view,permission_classes
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt
from core.models import Proveedor
from .serializers import ProveedorSerializer

from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated

@csrf_exempt
@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticated])
def lista_proveedores(request):
    """
    Lista todos los vehiculos
    """
    if request.method == 'GET':
        proveedor = Proveedor.objects.all()
        serializer = ProveedorSerializer(proveedor, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = ProveedorSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@csrf_exempt
@api_view(['GET', 'PUT', 'DELETE'])
@permission_classes([IsAuthenticated])
def detalle_proveedores(request, id):
    """
    get, update, delete de un proveedor en particular
    """
    try:
        proveedor = Proveedor.objects.get(id_Proveedor = id)
    except Proveedor.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = ProveedorSerializer(proveedor)
        return Response(serializer.data)        
    if request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = ProveedorSerializer(proveedor, data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
    elif request.method == 'DELETE':
        proveedor.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)