__all__ = ['AddProductService']

from prismapp.models import Merchant, Category, Product, Hashtag, Keyword
from prismapp.modules.merchant.product.add_product.dtos import ProductInformation
from prismapp.modules.merchant.product.add_product.exceptions import MerchantDoesNotExist


class AddProductService:

    def add_product(self, user, product_info: ProductInformation):

        try:
            merchant = Merchant.objects.get(owner=user)
        except Merchant.DoesNotExist:
            raise MerchantDoesNotExist

        product = Product.objects.create(
            owner=user,
            merchant=merchant,
            name=product_info.name,
            quantity=product_info.quantity,
            unit=product_info.unit,
            description=product_info.description,
            description_html=product_info.description_html,
            original_price=product_info.original_price,
            discount_price=product_info.discount_price,
            images=product_info.images,
            total_bookings=product_info.total_bookings,
            hidden=product_info.hidden,
            sold_quantity=product_info.sold_quantity
        )

        if product_info.hashtags is not None:
            for hashtag in product_info.hashtags:
                if not Hashtag.objects.filter(name=hashtag).exists():
                    Hashtag.objects.create(name=hashtag)

                product.hashtags.add(Hashtag.objects.get(name=hashtag))

        if product_info.keywords is not None:
            for keyword in product_info.keywords:
                if not Keyword.objects.filter(name=keyword).exists():
                    Keyword.objects.create(name=keyword)
                product.keywords.add(Keyword.objects.get(name=keyword))

