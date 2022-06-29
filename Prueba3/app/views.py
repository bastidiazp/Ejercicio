from django.shortcuts import render, redirect, get_object_or_404
from .models import Producto
from .forms import FormularioForm, ProductoForm
from rest_framework import viewsets
from .serializers import ProductoSerializer

class ProductoViewset(viewsets.ModelViewSet):
    queryset = Producto.objects.all()
    serializer_class = ProductoSerializer

    def get_queryset(self):
        productos = Producto.objects.all()

        nombre = self.request.GET.get('nombre')

        if nombre: 
            productos = productos.filter(nombre__contains=nombre)

            return productos

# Create your views here.
def home(request):
    return render(request, 'app/home.html')

def productos(request):
    productos = Producto.objects.all()
    data = {
        'productos': productos
    }
    return render(request, 'app/productos.html', data)

def formulario(request):
    data = {
        'form': FormularioForm()
    }

    if request.method == 'POST':
        formulario = FormularioForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            data["mensaje"] = "Solicitud Exitosa"
        else:
            data["form"] = formulario

    return render(request, 'app/formulario.html', data)

def agregar_producto(request):
    data = {
        'form': ProductoForm()
    }

    if request.method == 'POST':
        formulario = ProductoForm(data=request.POST, files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            data["mensaje"] = "¡Agregado Exitosamente!"
        else:
            data["form"] = formulario

    return render(request, 'app/items/agregar.html', data)

def listar_producto(request):
    productos = Producto.objects.all()

    data = {
        'productos': productos
    }

    return render(request, 'app/items/listar.html', data)

def modificar_producto(request, id):

    producto = get_object_or_404(Producto, id=id)

    data = {
        'form': ProductoForm(instance=producto)
    }

    if request.method == 'POST':
        formulario = ProductoForm(data=request.POST, instance=producto, files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            return redirect(to="listar_producto")
        data["form"] = formulario

    return render(request, 'app/items/modificar.html', data)

def eliminar_producto(request, id):
    producto = get_object_or_404(Producto, id=id)
    producto.delete()
    return redirect(to="listar_producto")