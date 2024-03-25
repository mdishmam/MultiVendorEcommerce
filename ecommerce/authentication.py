from rest_framework.authentication import TokenAuthentication
from rest_framework import exceptions

class BuyerAuth(TokenAuthentication):

    def authenticate(self, request):
        (user, token) = super().authenticate(request)
        if user.type == user.BUYER:
            return (user, token)
        raise exceptions.AuthenticationFailed(('Not a buyer account.'))


class SellerAuth(TokenAuthentication):

    def authenticate(self, request):
        (user, token) = super().authenticate(request)
        if user.type == user.SELLER:
            return (user, token)
        raise exceptions.AuthenticationFailed(('Not a seller account.'))

