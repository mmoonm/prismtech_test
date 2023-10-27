from django.urls import path, include
from prismapp.modules.merchant.add_product.view import AddProduct
from prismapp.modules.merchant.create_merchant.view import CreateMerchant
from prismapp.modules.merchant.remove_product.view import RemoveProduct

urlpatterns = [
    path('add-product/', AddProduct.as_view()),
    path('remove-product/', RemoveProduct.as_view()),
    path('create-merchant/', CreateMerchant.as_view()),
]
