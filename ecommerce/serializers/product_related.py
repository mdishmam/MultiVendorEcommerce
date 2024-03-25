from rest_framework import serializers

from ecommerce.models import Product


class AllProductsSerializer(serializers.ModelSerializer):

    seller = serializers.CharField(source='user')
    class Meta:
        model = Product
        fields = ('name', 'description', 'image', 'price', 'quantity_at_present', 'seller')