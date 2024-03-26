from rest_framework import status
from rest_framework.response import Response

from config.base_views import BuyerAuthenticationView
from rest_framework.generics import GenericAPIView, ListAPIView, UpdateAPIView, CreateAPIView, RetrieveAPIView

from ecommerce.models import Product, Cart
from ecommerce.serializers import AllProductsSerializer, SingleProductInCartSerializer, CartSerializer


class ProductListAll(ListAPIView):
    queryset = Product.objects.all()
    serializer_class = AllProductsSerializer


class AddToCart(BuyerAuthenticationView, CreateAPIView):
    serializer_class = SingleProductInCartSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        try:
            instance = serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)


class GetCart(BuyerAuthenticationView, RetrieveAPIView):
    serializer_class = CartSerializer

    def get_object(self):
        return Cart.objects.get(user=self.request.user)