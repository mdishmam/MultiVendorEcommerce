from django.contrib.auth.models import AbstractUser
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from config.base_models import SellerUserMixin, TimeStampMixin


class User(AbstractUser):
    BUYER = 'buyer'
    SELLER = 'seller'
    user_type_choices = [
        (BUYER, 'Buyer'),
        (SELLER, 'Seller')
    ]
    type = models.CharField(max_length=50, choices=user_type_choices)


class DailyRevenue(SellerUserMixin, TimeStampMixin):
    orders = models.ManyToManyField('Order', related_name='dailyrevenue_orders')
    total_sell = models.FloatField(default=0)
    total_buying_price = models.FloatField(default=0)

    def __str__(self):
        return self.user.username



@receiver(post_save, sender=User)
def create_spot_market(sender, instance=None, created=False, **kwargs):
    from ecommerce.models import Cart
    if created:
        if instance.type == User.BUYER:
            Cart.objects.create(user=instance)