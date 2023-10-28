__all__ = ['CreateMerchantService']

from prismapp.models import Merchant, Keyword, Hashtag, Category
from prismapp.modules.merchant.create_merchant.dtos import MerchantInformation
from prismapp.modules.merchant.create_merchant.exceptions import UserAlreadyHasAMerchant
import uuid

class CreateMerchantService:

    def create_merchant(self, user, merchant_info: MerchantInformation):

        if Merchant.objects.filter(owner=user).exists():
            raise UserAlreadyHasAMerchant
        else:
            merchant = Merchant.objects.create(
                owner=user,
                name=merchant_info.name,
                uid=self._generate_uid(),
                # ...
            )

            if merchant_info.hashtags is not None:
                for hashtag in merchant_info.hashtags:
                    if not Hashtag.objects.filter(name=hashtag).exists():
                        Hashtag.objects.create(name=hashtag)

                    merchant.hashtags.add(Hashtag.objects.get(name=hashtag))
            if merchant_info.keywords is not None:
                for keyword in merchant_info.keywords:
                    if not Keyword.objects.filter(name=keyword).exists():
                        Keyword.objects.create(name=keyword)
                    merchant.keywords.add(Keyword.objects.get(name=keyword))

            if merchant_info.categories is not None:
                for category in merchant_info.categories:
                    if Keyword.objects.filter(name=category).exists():
                        merchant.categories.add(Keyword.objects.get(name=category))



    def _generate_uid(self):
        return "Mer_" + str(uuid.uuid4())
