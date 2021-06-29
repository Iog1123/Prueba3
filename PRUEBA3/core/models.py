from django.db import models


# Create your models here.
class Pais(models.Model):
     id_pais=models.IntegerField(primary_key=True,unique=True,verbose_name="id pais")
     nombre_pais=models.CharField(max_length=50, null=False, verbose_name="nombre del pais")

     def __str__(self):
        return self.nombre_pais

   


class Proveedor(models.Model):
    id_Proveedor=models.IntegerField(primary_key=True, verbose_name="id de proveedor")
    nombreCompleto=models.CharField(max_length=50,null=False, verbose_name="nombre completo proveedor")
    telefono=models.IntegerField(null=False,unique=True)
    direccion=models.CharField(max_length=100,null=False, unique=True, verbose_name="direccion proveedor")
    email=models.CharField(max_length=100,null=False,unique=True,verbose_name="dirección correo electronico")
    password=models.CharField(max_length=8,null=False)
    Pais= models.ForeignKey(Pais, on_delete=models.CASCADE)


    def __str__(self):
        return self.nombreCompleto
