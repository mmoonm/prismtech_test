__all__ = ['RemovePromotionService']

from prismapp.models import Merchant, Promotion, Hashtag, Keyword
from prismapp.modules.merchant.promotion.remove_promotion.dtos import PromotionInformation
from prismapp.modules.merchant.promotion.remove_promotion.exceptions import MerchantDoesNotExist


class RemovePromotionService:

    def remove_promotion(self, user, promotion_info: PromotionInformation):

        try:
            merchant = Merchant.objects.get(owner=user)
        except Merchant.DoesNotExist:
            raise MerchantDoesNotExist

        promotion = Promotion.objects.filter(
            owner=user,
            merchant=merchant,
            name=promotion_info.name
        )

        if promotion is not None:
            promotion.delete()
