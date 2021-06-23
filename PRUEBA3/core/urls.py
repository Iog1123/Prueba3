from django.urls import path
from .views import form_datos, index, proveedor

urlpatterns = [
    path('', index, name="index"),
    path('proveedor', proveedor, name="proveedor"),
    path('form_datos', form_datos,name="form_datos")
        
]
  