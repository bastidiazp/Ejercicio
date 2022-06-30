from .models import Producto, Tipo
from rest_framework import serializers

class TipoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tipo
        fields = '__all__'

class ProductoSerializer(serializers.ModelSerializer):    
    nombre_tipo = serializers.CharField(read_only=True, source="tipo.nombre")
    tipo = TipoSerializer(read_only=True)
    tipo_id = serializers.PrimaryKeyRelatedField(queryset=Tipo.objects.all(), source="tipo")
    nombre = serializers.CharField(required=True, min_length=3)

    def validate_nombre(self, value):
        existe = Producto.objects.filter(nombre__iexact=value).exists()

        if existe:
            raise serializers.ValidationError("Este producto ya esta ingresado.")

        return value

    class Meta:
        model = Producto
        fields = '__all__'