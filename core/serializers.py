from rest_framework import serializers
from django.db.models import Sum

from .models import Client, Product, Sale, SaleProduct


class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        extra_kwargs = {
            'email': {'write_only': True},
            'cpf': {'write_only': True},
        }
        model = Client
        fields = (
            'id',
            'full_name',
            'date_of_birth',
            'sex',
            'phone',
            'email',
            'cpf',
            'indebted',
        )


class SaleProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = SaleProduct
        fields = (
            'id',
            'product',
            'sale',
            'amount',
        )


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = (
            'id',
            'name',
            'type',
            'price',
            'amount',
            'image',
            'active',
        )


class SaleSerializer(serializers.ModelSerializer):
    products = ProductSerializer(many=True, read_only=True)
    sale_products = SaleProductSerializer(many=True, read_only=True)
    total = serializers.SerializerMethodField()

    class Meta:
        model = Sale
        fields = (
            'id',
            'client',
            'user',
            'products',
            'date',
            'purchase_type',
            'total',
            'sale_products',
        )

    def get_total(self, obj):
        sum_total = obj.products.aggregate(Sum('price')).get('price__sum')
        return sum_total

