from django.urls import path
from . import views

urlpatterns = [
    path('signup/', views.SignUpView.as_view(), name="sign_up"),
    path('signin/', views.SignInView.as_view(), name="sign_in"),

    path('get-all-products/', views.ProductListAll.as_view(), name="get_all_products"),
    path('add-to-cart/', views.AddToCart.as_view(), name="add_to_cart"),
    path('view-cart/', views.GetCart.as_view(), name="view_cart"),

    path('products/', views.AllProductsView.as_view(), name="view_app_products")
]