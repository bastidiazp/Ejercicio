from unittest.util import _MAX_LENGTH
from django.db import models
from django.forms import PasswordInput

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
    imagen = models.ImageField(upload_to="productos", null=True)

    def __str__(self):
        return self.nombre

###################
#FORMULARIO

opciones_pais = [
    [0, "Chile"],
    [1, "Argentina"],
    [2, "España"]
]

opciones_region = [
    [0, "Antofagasta"],
    [1, "Valparaíso"],
    [2, "Araucanía"]
]

opciones_flores = [
    [0, "Lilys"],
    [1, "Girasoles"],
    [2, "Rosas"],
    [3, "Tulipanes"],
    [4, "Jasmines"],
    [5, "Gladiolas"],
    [6, "Hibiscus"],
    [7, "Violetas"]
]

opciones_espe = [
    [0, "Arbustos"],
    [1, "Flores"],
    [2, "Maceteros"],
    [3, "Tierra de Hojas"]
]

class Formulario(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    edad = models.IntegerField()
    direccion = models.CharField(max_length=100)
    tipo_pais = models.IntegerField(choices=opciones_pais)
    tipo_region = models.IntegerField(choices=opciones_region)
    tipo_flores = models.IntegerField(choices=opciones_flores)
    tipo_especializacion = models.IntegerField(choices=opciones_espe)
    correo = models.EmailField()
    contraseña = models.CharField(max_length=50)

    def __str__(self):
        return self.nombre