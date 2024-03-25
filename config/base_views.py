from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from ecommerce.authentication import BuyerAuth, SellerAuth


class BuyerAuthenticationView:
    authentication_classes = [BuyerAuth]
    permission_classes = [IsAuthenticated]


class SellerAuthenticationView:
    authentication_classes = [SellerAuth]
    permission_classes = [IsAuthenticated]