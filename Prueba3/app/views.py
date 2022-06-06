from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'app/home.html')

def productos(request):
    return render(request, 'app/productos.html')

def formulario(request):
    return render(request, 'app/formulario.html')