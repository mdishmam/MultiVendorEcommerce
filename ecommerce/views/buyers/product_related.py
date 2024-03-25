from config.base_views import BuyerAuthenticationView
from rest_framework.generics import GenericAPIView, ListAPIView, UpdateAPIView, CreateAPIView

from ecommerce.models import Product
from ecommerce.serializers import AllProductsSerializer, SingleProductInCartSerializer


class ProductListAll(ListAPIView):
    queryset = Product.objects.all()
    serializer_class = AllProductsSerializer


class AddToCart(BuyerAuthenticationView, CreateAPIView):
    serializer_class = SingleProductInCartSerializer
    # def post(self, request, *args, **kwargs):
    #     pass