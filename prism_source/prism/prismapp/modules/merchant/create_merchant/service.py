__all__ = ['CreateMerchantService']

from prismapp.models import Merchant
from prismapp.modules.merchant.create_merchant.dtos import MerchantInformation


class CreateMerchantService:

    def create_merchant(self, user, merchant_info: MerchantInformation):

        if not Merchant.objects.filter(owner=user).exists():
            print("HAHAHAHAa")

        merchant = Merchant.objects.create(
            owner=user,
            name=merchant_info.data.get('name'),
        )
        return True
