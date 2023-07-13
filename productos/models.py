import datetime
from django.db import models

# Create your models here.
class Categoria(models.Model):
    idCategoria = models.IntegerField(primary_key=True, verbose_name="Id de Categoria")
    nombreCategoria = models.CharField(max_length=50, blank=True, verbose_name="Nombre de Categoria")

    def __str__(self):
        return str(self.nombreCategoria)

class Producto(models.Model):
    nombre_producto = models.CharField(max_length=100, blank=True, verbose_name="Nombre del Producto")
    nro_producto = models.IntegerField(primary_key=True, verbose_name="Nro producto")
    descripcion = models.CharField(max_length=100, blank=True, verbose_name="Descripcion")
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE, verbose_name="Categoria")
    precio = models.IntegerField(blank=True, null=True, verbose_name="Precio")
    imagen=models.ImageField(upload_to="imagenes",null=True, blank=True,verbose_name="Imagen")

    def __str__(self):
        return str(self.nro_producto)

class Boleta(models.Model):
    id_boleta = models.AutoField(primary_key=True)
    total = models.BigIntegerField()
    fechaCompra = models.DateTimeField(blank=False, null=False, default = datetime.datetime.now)

    def __str__(self):
        return str(self.id_boleta)

class detalle_boleta(models.Model):
    id_boleta = models.ForeignKey('Boleta', blank=True, on_delete=models.CASCADE)
    id_detalle_boleta = models.AutoField(primary_key=True)
    id_producto = models.ForeignKey('Producto', on_delete=models.CASCADE)
    cantidad = models.IntegerField()
    subtotal = models.BigIntegerField()

    def __str__(self):
        return str(self.id_detalle_boleta)