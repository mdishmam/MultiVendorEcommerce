from rest_framework import serializers

from ecommerce.models import Product, Cart, SingleProductInCart, User


class AllProductsSerializer(serializers.ModelSerializer):

    seller = serializers.CharField(source='user')
    class Meta:
        model = Product
        fields = ('name', 'description', 'image', 'price', 'quantity_at_present', 'seller')


# class CartSerializer(serializers.ModelSerializer):
#     buyer = serializers.CharField(source='user')
#     class Meta:
#         model = Cart
#         fields = ('buyer')

class SingleProductInCartSerializer(serializers.ModelSerializer):
    user = serializers.SerializerMethodField()
    class Meta:
        model = SingleProductInCart
        fields = ('user', 'product', 'quantity', 'user_id')
        extra_kwargs = {"user_id": {"write_only": True}}

    def get_user(self, obj):
        return obj.cart.user

    def create(self, validated_data):
        user = validated_data.pop('user_id', None)
        if user:
            validated_data["cart"] = Cart.objects.get(user_id=user)
        single_product_in_cart = SingleProductInCart.objects.create(**validated_data)
        return single_product_in_cart


class CartSerializer(serializers.ModelSerializer):
    products_in_cart = SingleProductInCartSerializer(source='singleproductincart_set', many=True, read_only=True)

    class Meta:
        model = Cart
        fields = ['id', 'user', 'products_in_cart']