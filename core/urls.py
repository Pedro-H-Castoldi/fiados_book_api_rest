from django.urls import path
from rest_framework.routers import SimpleRouter

from .views import ClientViewSet, ProductViewSet, SaleViewSet, SaleProductViewSet


router = SimpleRouter()
router.register('client', ClientViewSet)
router.register('product', ProductViewSet)
router.register('sale', SaleViewSet)
router.register('sale_product', SaleProductViewSet)

