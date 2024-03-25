from django.contrib import admin
from django.utils.html import format_html

from .models import *

# Register your models here.
@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'type')
    list_filter = ('type',)


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'unit', 'colored_quantity', 'user')
    list_filter = ('user__username',)

    @admin.display(description='Quantity')
    def colored_quantity(self, obj):
        if obj.quantity_at_present < obj.minimum_quantity:
            return format_html(
                '<span style="color: #FF0000;">{}</span>',
                obj.quantity_at_present,
            )
        else:
            return format_html(
                '<span style="color: #000000;">{}</span>',
                obj.quantity_at_present,
            )

    def get_queryset(self, request):
        if not request.user.is_superuser:
            return Product.objects.filter(user=request.user)
        return Product.objects.all()


@admin.register(Unit)
class UnitAdmin(admin.ModelAdmin):
    pass