from django.db import models
from config.base_models import BuyerUserMixin, TimeStampWithUpdateMixin
from ecommerce.models import Product


class SingleOrder(models.Model):
    order = models.ForeignKey('Order', on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField()

    def __str__(self):
        return self.product.name


class Order(BuyerUserMixin, TimeStampWithUpdateMixin):
    PENDING = 'pending'
    CHECKED = 'checked'


    order_status_choices = [
        (PENDING, 'Pending'),
        (CHECKED, 'Checked')
    ]

    status = models.CharField(max_length=100, choices=order_status_choices)

    def __str__(self):
        return f"{self.user.username} - {self.created_at}"


