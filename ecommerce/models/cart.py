from django.db import models

from config.base_models import BuyerUserMixinOneToOne, TimeStampWithUpdateMixin
from .product import Product


class SingleProductInCart(models.Model):
    cart = models.ForeignKey('Cart', on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)

    def __str__(self):
        return self.product.name


class Cart(BuyerUserMixinOneToOne, TimeStampWithUpdateMixin):

    def __str__(self):
        return self.user.username

