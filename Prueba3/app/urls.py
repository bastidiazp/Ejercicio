from django.urls import path
from .views import home, productos, formulario

urlpatterns = [
    path('', home, name="home"),
    path('productos/', productos, name="productos"),
    path('formulario/', formulario, name="formulario"),
]