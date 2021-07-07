from django.urls import path
from .views import contacto, form_datos, form_del_proveedor, form_mod_proveedor, index, proveedor, somos, tabla1, tabla2, tabla3

urlpatterns = [
    path('', index, name="index"),
    path('proveedor', proveedor, name="proveedor"),
    path('form_datos', form_datos,name="form_datos"),
    path('form_mod_proveedor/<id>', form_mod_proveedor, name="form_mod_proveedor"),
    path('form_del_proveedor/<id>', form_del_proveedor, name="form_del_proveedor"),
    path('tabla1',tabla1,name="tabla1"),
    path('tabla2',tabla2,name="tabla2"),
    path('tabla3',tabla3,name="tabla3"),
    path('somos',somos,name="somos"),
    path('contacto', contacto,name="contacto")    
]
  