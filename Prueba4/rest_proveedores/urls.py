from django.urls import path
from rest_proveedores.views import lista_proveedores, detalle_proveedores
from rest_proveedores.viewsLogin import login

urlpatterns = [
    path('lista_proveedores', lista_proveedores, name="lista_proveedores"),
    path('detalle_proveedores/<id>', detalle_proveedores, name="detalle_proveedores"),
    path('login', login, name="login"),
]