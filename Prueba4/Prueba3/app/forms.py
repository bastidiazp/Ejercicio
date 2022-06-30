from dataclasses import fields
from unittest.util import _MAX_LENGTH
from django import forms
from .models import Formulario, Producto
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .validators import MaxSizeFileValidator
from django.forms import ValidationError

class FormularioForm(forms.ModelForm):

    class Meta:
        model = Formulario
        #fields = ["nombre", "apellido", "edad", "direccion", "tipo_pais", "tipo_region", "tipo_flores", "tipo_especializacion", "correo", "contraseña"]
        fields = '__all__'

class ProductoForm(forms.ModelForm):

    ##### VALIDACIONES (USAR FORMS MODELS.PY DE REFERENCIA)
    nombre = forms.CharField(min_length=3, max_length=50)
    especie = forms.CharField(min_length=3, max_length=50)
    #descripcion = forms.TextField(min_length=3, max_length=1000)
    precio = forms.IntegerField(min_value=1, max_value=2000000)
    #novedad
    #tipo
    #fecha_entrada
    imagen = forms.ImageField(required=False, validators=[MaxSizeFileValidator(max_file_size=3)])

    def clean_nombre(self):
        nombre = self.cleaned_data["nombre"]
        existe = Producto.objects.filter(nombre__iexact=nombre).exists()

        if existe:
            raise ValidationError("Este nombre ya existe")

        return nombre

    class Meta:
        model = Producto
        fields = '__all__'

class CustomUserCreationForm(UserCreationForm):

    class Meta:
        model = User
        fields = ['username', "first_name", "last_name", "email", "password1", "password2"]