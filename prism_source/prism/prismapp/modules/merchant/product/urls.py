from django.urls import path, include
from prismapp.modules.merchant.product.add_product.view import AddProduct
from prismapp.modules.merchant.product.remove_product.view import RemoveProduct

urlpatterns = [
    path('add-product/', AddProduct.as_view()),
    path('remove-product/', RemoveProduct.as_view()),
]
