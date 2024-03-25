from django.urls import path
from . import views

urlpatterns = [
    path('signup/', views.SignUpView.as_view(), name="sign_up"),
    path('signin/', views.SignInView.as_view(), name="sign_in"),

    path('get-all-products/', views.ProductListAll.as_view(), name="get_all_products")
]