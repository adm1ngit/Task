from rest_framework import serializers
from .models import Product, Material, ProductMaterial

class MaterialSerializer(serializers.ModelSerializer):
    class Meta:
        model = Material
        fields = ['id', 'name', 'warehouse', 'remaining_quantity', 'price']

class ProductMaterialSerializer(serializers.ModelSerializer):
    material = MaterialSerializer()

    class Meta:
        model = ProductMaterial
        fields = ['material', 'quantity']

class ProductSerializer(serializers.ModelSerializer):
    materials = ProductMaterialSerializer(many=True)

    class Meta:
        model = Product
        fields = ['id', 'name', 'quantity', 'materials']
