from django.db.models import Sum, F
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
    # user = serializers.SerializerMethodField()
    product_name = serializers.SerializerMethodField()
    product_image = serializers.SerializerMethodField()
    product_description = serializers.SerializerMethodField()
    product_price = serializers.SerializerMethodField()

    class Meta:
        model = SingleProductInCart
        fields = ('product', 'product_name', 'quantity', 'product_image', 'product_description', 'product_price')
        # fields = ('user', 'product', 'quantity')
        extra_kwargs = {"product": {"write_only": True}}

    def get_user(self, obj):
        return obj.cart.user.username

    def get_product_name(self, obj):
        return obj.product.name

    def get_product_image(self, obj):
        if obj.product.image:
            return obj.product.image.url
        return None

    def get_product_description(self, obj):
        return obj.product.description

    def get_product_price(self, obj):
        return obj.product.price


    def create(self, validated_data):
        request = self.context["request"]
        user = request.user
        if user:
            validated_data["cart"] = Cart.objects.get(user=user)
            print(validated_data)
        single_product_in_cart = SingleProductInCart.objects.create(**validated_data)
        return single_product_in_cart


class CartSerializer(serializers.ModelSerializer):
    products_in_cart = SingleProductInCartSerializer(source='singleproductincart_set', many=True, read_only=True)
    total_price = serializers.SerializerMethodField()

    class Meta:
        model = Cart
        fields = ['id', 'total_price', 'products_in_cart']

    def get_total_price(self, obj):
        total = obj.singleproductincart_set.aggregate(total_price=Sum(F('product__price') * F('quantity')))[
                    'total_price'] or 0
        return total