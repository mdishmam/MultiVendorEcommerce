# core/views.py

from django.views.generic import ListView
from ..models import Product

class AllProductsView(ListView):
    model = Product
    template_name = "ecommerce/index.html"
    context_object_name = "products"
    paginate_by = 10
    ordering = "pk"

    # new method added ⬇️
    def get_template_names(self, *args, **kwargs):
        if self.request.htmx:
            return "ecommerce/product-list.html"
        else:
            return self.template_name

