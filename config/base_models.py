from django.db import models
from django.conf import settings
from django.utils import timezone


class UserMixin(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    class Meta:
        abstract = True

class SellerUserMixin(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, limit_choices_to={'type':'seller'}, on_delete=models.CASCADE)

    class Meta:
        abstract = True


class BuyerUserMixin(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, limit_choices_to={'type': 'buyer'}, on_delete=models.CASCADE)

    class Meta:
        abstract = True


class BuyerUserMixinOneToOne(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, limit_choices_to={'type': 'buyer'}, on_delete=models.CASCADE)

    class Meta:
        abstract = True

class TimeStampMixin(models.Model):
    created_at = models.DateTimeField(default=timezone.now)

    class Meta:
        abstract = True


class TimeStampWithUpdateMixin(TimeStampMixin):
    updated_at = models.DateTimeField(default=timezone.now)

    class Meta:
        abstract = True

    def save(self, *args, **kwargs):
        self.updated_at = timezone.now()
        return super().save(*args, **kwargs)
