from django.db import models

# Create your models here.
class Tipo(models.Model): #TIPO = ARBUSTO, FLORES, MACETEROS, TIERRAS
    nombre = models.CharField(max_length=50)

    def __str__(self):
        return self.nombre

class Producto(models.Model): #PRODUCTO = NOMBRE, ESPECIE, DESCRIPCION, PRECIO, NOVEDAD, TIPO, FECHA DE ENTRADA A TIENDA
    nombre = models.CharField(max_length=50)
    especie = models.CharField(max_length=50)
    descripcion = models.TextField()
    precio = models.IntegerField()
    novedad = models.BooleanField()
    tipo = models.ForeignKey(Tipo, on_delete=models.PROTECT)
    fecha_entrada = models.DateField()

    def __str__(self):
        return self.nombre