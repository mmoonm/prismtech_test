__all__ = ['RemoveProductService']

from prismapp.models import Merchant, Product, Hashtag, Keyword
from prismapp.modules.merchant.product.remove_product.dtos import ProductInformation
from prismapp.modules.merchant.product.remove_product.exceptions import MerchantDoesNotExist


class RemoveProductService:

    def remove_product(self, user, product_info: ProductInformation):

        try:
            merchant = Merchant.objects.get(owner=user)
        except Merchant.DoesNotExist:
            raise MerchantDoesNotExist

        product = Product.objects.filter(
            owner=user,
            merchant=merchant,
            name=product_info.name
        )

        if product is not None:
            product.delete()
