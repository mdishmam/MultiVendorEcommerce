from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from config.base_views import BuyerAuthenticationView
from rest_framework.generics import GenericAPIView, ListAPIView, UpdateAPIView, CreateAPIView, RetrieveAPIView

from ecommerce.models import Product, Cart, Order, SingleOrder
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

class OrderProducts(BuyerAuthenticationView, APIView):
    def get(self, request, *args, **kwargs):
        cart = Cart.objects.get(user=request.user)
        order = Order.objects.create(user=request.user, status=Order.PENDING)

        for cart_element in cart.singleproductincart_set.all():
            SingleOrder.objects.create(
                order=order,
                product=cart_element.product,
                quantity=cart_element.quantity
            )
            product = cart_element.product
            product.quantity_at_present -= cart_element.quantity
            product.save()
            cart_element.delete()

        return Response({'status':'order placed successfully.'})