from config.base_views import BuyerAuthenticationView
from rest_framework.generics import ListAPIView

from ecommerce.models import Product
from ecommerce.serializers import AllProductsSerializer


class ProductListAll(ListAPIView):
    queryset = Product.objects.all()
    serializer_class = AllProductsSerializer