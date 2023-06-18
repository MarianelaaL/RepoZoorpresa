from django.db import models

# Create your models here.
class Categoria(models.Model):
    idCategoria = models.IntegerField(primary_key=True, verbose_name="Id de Categoria")
    nombreCategoria = models.CharField(max_length=50, blank=True, verbose_name="Nombre de Categoria")

    def __str__(self):
        return str(self.idCategoria)

class Producto(models.Model):
    nombre_producto = models.CharField(max_length=100, blank=True, verbose_name="Nombre del Producto")
    nro_producto = models.IntegerField(primary_key=True, max_length=3, verbose_name="Nro producto")
    descripcion = models.CharField(max_length=100, blank=True, verbose_name="Descripcion")
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE, verbose_name="Categoria")
    precio = models.IntegerField(max_length=7, blank=True, verbose_name="Precio")
    cantidad = models.IntegerField(max_length=7, blank=True, verbose_name="Cantidad")
    imagen=models.ImageField(upload_to="imagenes",null=True, blank=True,verbose_name="Imagen")

    def __str__(self):
        return str(self.nro_producto)
