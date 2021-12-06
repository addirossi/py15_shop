from rest_framework import serializers


# class ProductSerializer(serializers.Serializer):
#     id = serializers.IntegerField()
#     name = serializers.CharField()
#     price = serializers.DecimalField(max_digits=10,
#                                      decimal_places=2)
#
#
# class ProductDetailsSerializer(serializers.Serializer):
#     id = serializers.IntegerField()
#     name = serializers.CharField()
#     description = serializers.CharField()
#     price = serializers.DecimalField(max_digits=10,
#                                      decimal_places=2)
from product.models import Product, Category


class ProductsListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ('id', 'name', 'price')


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'
