from rest_framework.decorators import api_view
from rest_framework.generics import ListAPIView, RetrieveAPIView, CreateAPIView, UpdateAPIView, DestroyAPIView, \
    ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet

from product.models import Product, Category
from product.serializers import ProductSerializer, ProductsListSerializer, CategorySerializer


# @api_view(['GET'])
# def products_list(request):
#     products = Product.objects.all()
#     serializer = ProductSerializer(products, many=True)
#     return Response(serializer.data)
#
#
# class ProductsListView(APIView):
#     def get(self, request):
#         products = Product.objects.all()
#         serializer = ProductSerializer(products, many=True)
#         return Response(serializer.data)


# CRUD (Create, Retrieve, Update, Delete)
# class ProductsListView(ListAPIView):
#     queryset = Product.objects.all()
#     serializer_class = ProductsListSerializer
#
#
# class ProductDetailsView(RetrieveAPIView):
#     queryset = Product.objects.all()
#     serializer_class = ProductSerializer
#
#
# class CreateProductView(CreateAPIView):
#     queryset = Product.objects.all()
#     serializer_class = ProductSerializer
#
#
# class UpdateProductView(UpdateAPIView):
#     queryset = Product.objects.all()
#     serializer_class = ProductSerializer
#
#
# class DeleteAPIView(DestroyAPIView):
#     queryset = Product.objects.all()
#     serializer_class = ProductSerializer
#
#
# class ProductListCreateView(ListCreateAPIView):
#     queryset = Product.objects.all()
#     serializer_class = ProductSerializer
#
#
# class ProductRetrieveUpdateDeleteView(RetrieveUpdateDestroyAPIView):
#     queryset = Product.objects.all()
#     serializer_class = ProductSerializer


class ProductViewSet(ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class CategoryViewSet(ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


# TODO: Авторизация
# TODO: Фильтрация продуктов
# TODO: Поиск по продуктам
# TODO: Пагинация
# TODO: Заказы
# TODO: Тесты
# TODO: git
# TODO: документация
