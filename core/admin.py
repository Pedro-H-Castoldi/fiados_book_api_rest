from django.contrib import admin
from .models import Client, Product, Sale, SaleProduct


@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'sex', 'phone', 'indebted', 'created', 'active')


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'type', 'price', 'amount', 'created', 'active')


@admin.register(Sale)
class PurchaseAdmin(admin.ModelAdmin):
    list_display = ('client', 'user', 'date', 'purchase_type')


@admin.register(SaleProduct)
class SaleProductAdmin(admin.ModelAdmin):
    list_display = ('product', 'sale', 'amount')