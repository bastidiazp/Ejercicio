from dataclasses import fields
from django import forms
from .models import Formulario, Producto

class FormularioForm(forms.ModelForm):

    class Meta:
        model = Formulario
        #fields = ["nombre", "apellido", "edad", "direccion", "tipo_pais", "tipo_region", "tipo_flores", "tipo_especializacion", "correo", "contraseña"]
        fields = '__all__'

class ProductoForm(forms.ModelForm):

    class Meta:
        model = Producto
        fields = '__all__'