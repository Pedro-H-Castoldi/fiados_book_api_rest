from django.shortcuts import render
from rest_framework import viewsets

from .serializers import ClientSerializer, ProductSerializer, SaleSerializer, SaleProductSerializer
from .models import Client, Product, Sale, SaleProduct


class ClientViewSet(viewsets.ModelViewSet):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer


class SaleProductViewSet(viewsets.ModelViewSet):
    queryset = SaleProduct.objects.all()
    serializer_class = SaleProductSerializer


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class SaleViewSet(viewsets.ModelViewSet):
    queryset = Sale.objects.all()
    serializer_class = SaleSerializer


