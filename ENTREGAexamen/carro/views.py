from django.shortcuts import render

from .carro import Carro

from app.models import Producto

from django.shortcuts import redirect

# Create your views here.

def agregar_producto(request, productos_nombre):

    carro=Carro(request)

    productos=Producto.objects.get(nombre=productos_nombre)

    carro.agregar(productos=productos)

    return redirect("app")

def eliminar_producto(request, productos_nombre):

    carro=Carro(request)

    productos=Producto.objects.get(nombre=productos_nombre)

    carro.eliminar(productos=productos)

    return redirect("app")

def restar_producto(request, productos_nombre):

    carro=Carro(request)

    productos=Producto.objects.get(nombre=productos_nombre)

    carro.restar_producto(productos=productos)

    return redirect("app")

def limpiar_carro(request, productos_nombre):

    carro=Carro(request)

    carro.limpiar_carro()

    return redirect("app")


