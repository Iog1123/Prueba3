# Generated by Django 3.2.3 on 2021-07-07 02:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Pais',
            fields=[
                ('id_pais', models.IntegerField(primary_key=True, serialize=False, verbose_name='id pais')),
                ('nombre_pais', models.CharField(max_length=50, verbose_name='nombre del pais')),
            ],
        ),
        migrations.CreateModel(
            name='Proveedor',
            fields=[
                ('id_Proveedor', models.AutoField(primary_key=True, serialize=False, verbose_name='id de proveedor')),
                ('nombreCompleto', models.CharField(max_length=50, verbose_name='nombre completo proveedor')),
                ('telefono', models.IntegerField()),
                ('direccion', models.CharField(max_length=100, verbose_name='direccion proveedor')),
                ('email', models.CharField(max_length=100, verbose_name='dirección correo electronico')),
                ('password', models.CharField(max_length=8)),
                ('Pais', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.pais')),
            ],
        ),
    ]
