
from rest_framework import serializers
from .models import *

class ProductsSerializers(serializers.ModelSerializer):
    class Meta:
        model = Products
        fields = "__all__"
        depth = 1

class CategorySerializers(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = "__all__"

class PedidosSerializers(serializers.ModelSerializer):
    class Meta:
        model = Pedido
        fields = "__all__"
    
    def validate(self, data):
        if not data["nombre"]:
            raise serializers.ValidationError({"nombre": "Este campo no puede estar vacío"})
        if data["telefono"] < 9999999:
            raise serializers.ValidationError({"telefono": "Debe introducir un número de teléfono válido"})
        if not data["direccion"]:
            raise serializers.ValidationError({"direccion": "Este campo no puede estar vacío"})
        if not data["productos"]:
            raise serializers.ValidationError({"productos": "Este campo no puede estar vacío"})
        return data
