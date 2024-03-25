from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    BUYER = 'buyer'
    SELLER = 'seller'
    user_type_choices = [
        (BUYER, 'Buyer'),
        (SELLER, 'Seller')
    ]
    type = models.CharField(max_length=50, choices=user_type_choices)
