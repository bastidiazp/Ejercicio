from django.shortcuts import render, redirect, get_object_or_404
from .models import Producto, Tipo
from .forms import FormularioForm, ProductoForm, CustomUserCreationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required, permission_required
from rest_framework import viewsets
from .serializers import ProductoSerializer, TipoSerializer

# Create your views here.


class TipoViewset(viewsets.ModelViewSet):
    queryset = Tipo.objects.all()
    serializer_class = TipoSerializer

class ProductoViewset(viewsets.ModelViewSet):
    queryset = Producto.objects.all()
    serializer_class = ProductoSerializer

    def get_queryset(self):
        productos = Producto.objects.all()
        nombre = self.request.GET.get('nombre')

        if nombre:
            productos = productos.filter(nombre__contains=nombre)

        return productos


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

###OTORGAR PERMISOS (LINEA 6)
@permission_required('app.add_producto')
def agregar_producto(request):
    data = {
        'form': ProductoForm()
    }

    if request.method == 'POST':
        formulario = ProductoForm(data=request.POST, files=request.FILES)
        if formulario.is_valid():
            formulario.save()

            ##### INCORPORACION MENSAJE AGREGAR
            messages.success(request, "¡Producto Agregado Exitosamente!")
            ###data["mensaje"] = "¡Agregado Exitosamente!" # FORMA ANTIGUA DE MOSTRAR MENSAJE
            
        else:
            data["form"] = formulario

    return render(request, 'app/items/agregar.html', data)

###OTORGAR PERMISOS (LINEA 6)
@permission_required('app.view_producto')
def listar_producto(request):
    productos = Producto.objects.all()

    data = {
        'productos': productos
    }

    return render(request, 'app/items/listar.html', data)

###OTORGAR PERMISOS (LINEA 6)
@permission_required('app.change_producto')
def modificar_producto(request, id):

    producto = get_object_or_404(Producto, id=id)

    data = {
        'form': ProductoForm(instance=producto)
    }

    if request.method == 'POST':
        formulario = ProductoForm(data=request.POST, instance=producto, files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            
            ##### INCORPORACION MENSAJE MODIFICAR
            messages.success(request, "Modificado Correctamente")

            return redirect(to="listar_producto")
        data["form"] = formulario

    return render(request, 'app/items/modificar.html', data)

###OTORGAR PERMISOS (LINEA 6)
@permission_required('app.delete_producto')
def eliminar_producto(request, id):
    producto = get_object_or_404(Producto, id=id)
    producto.delete()

    ##### INCORPORACION MENSAJE ELIMINAR
    messages.success(request, "Eliminado Correctamente")
    
    return redirect(to="listar_producto")

def registro(request):
    data = {
        'form': CustomUserCreationForm()
    }

    if request.method == 'POST':
        formulario = CustomUserCreationForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            user = authenticate(username=formulario.cleaned_data["username"], password=formulario.cleaned_data["password1"])
            login(request, user)
            messages.success(request, "¡Te has registrado exitosamente!")
            ###REDIRECCIONAMIENTO HACIA HOME/INDEX
            return redirect(to="home")
        data["form"] = formulario

    return render(request, 'registration/registro.html', data)