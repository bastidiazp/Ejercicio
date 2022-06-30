from django.urls import path
from .views import home, productos, formulario, agregar_producto, listar_producto, modificar_producto, eliminar_producto,\
    registro

urlpatterns = [
    path('', home, name="home"),
    path('productos/', productos, name="productos"),
    path('formulario/', formulario, name="formulario"),
    path('agregar-producto/', agregar_producto, name="agregar_producto"),
    path('listar-producto/', listar_producto, name="listar_producto"),
    path('modificar-producto/<id>/', modificar_producto, name="modificar_producto"),
    path('eliminar-producto/<id>/', eliminar_producto, name="eliminar_producto"),
    path('registro/', registro, name="registro"),
]