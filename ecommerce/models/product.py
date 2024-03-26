from django.db import models

from config.base_models import TimeStampWithUpdateMixin, SellerUserMixin


class Unit(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Product(TimeStampWithUpdateMixin, SellerUserMixin):
    name = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(null=True, blank=True)
    price = models.FloatField()
    buy_price = models.FloatField()
    unit = models.ForeignKey(Unit, on_delete=models.CASCADE)

    quantity_at_present = models.FloatField(default=0)
    minimum_quantity = models.FloatField(default=0)

    def __str__(self):
        return self.name
