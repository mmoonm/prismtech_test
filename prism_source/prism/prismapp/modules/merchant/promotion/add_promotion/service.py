__all__ = ['AddPromotionService']

from prismapp.models import Merchant, Promotion, Product, Service
from prismapp.modules.merchant.promotion.add_promotion.dtos import PromotionInformation
from prismapp.modules.merchant.promotion.add_promotion.exceptions import MerchantDoesNotExist


class AddPromotionService:

    def add_promotion(self, user, promotion_info: PromotionInformation):

        try:
            merchant = Merchant.objects.get(owner=user)
        except Merchant.DoesNotExist:
            raise MerchantDoesNotExist

        promotion = Promotion.objects.create(
            owner=user,
            merchant=merchant,
            name=promotion_info.name,
            unit=promotion_info.unit,
            description=promotion_info.description,
            images=promotion_info.images,
            total_bookings=promotion_info.total_bookings,
        )

        if promotion_info.products is not None:
            for product in promotion_info.products:
                if not Product.objects.filter(name=product).exists():
                    Product.objects.create(name=product, merchant=merchant)

                promotion.products.add(Product.objects.get(name=product, merchant=merchant, id=1))

        if promotion_info.services is not None:
            for service in promotion_info.services:
                if not Service.objects.filter(name=service).exists():
                    Service.objects.create(name=service, time=1.0, available_slots=1, merchant=merchant)

                promotion.services.add(Service.objects.get(name=service, merchant=merchant))
