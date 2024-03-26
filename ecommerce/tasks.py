from django.db.models import Sum
from django.utils import timezone

from ecommerce.models import Order, User


def run_check_for_all_user():
    for user in User.objects.filter(type=User.SELLER):
        check_all_orders_of_user(user)


def check_all_orders_of_user(user: User):
    todays_orders = Order.objects.filter(created_at__date=timezone.now().date())
    # Iterate through each order
    total_price = 0
    for order in todays_orders:
        # Filter single orders associated with the specific user
        user_single_orders = order.singleorder_set.filter(product__user=user)

        # Calculate the total price for products in this order and owned by the specific user
        order_total_price = user_single_orders.aggregate(total_price=Sum('product__price' * 'quantity'))[
                                'total_price'] or 0

        # Add the order total price to the overall total price
        total_price += order_total_price

    todays_orders.update(status=Order.CHECKED)
    return total_price
