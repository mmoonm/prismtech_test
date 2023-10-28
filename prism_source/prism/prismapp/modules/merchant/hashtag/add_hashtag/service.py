__all__ = ['AddHashtagService']

from prismapp.models import Merchant, Hashtag
from prismapp.modules.merchant.hashtag.add_hashtag.dtos import HashtagInformation
from prismapp.modules.merchant.hashtag.add_hashtag.exceptions import MerchantDoesNotExist


class AddHashtagService:

    def add_hashtag(self, user, hashtag_info: HashtagInformation):

        try:
            merchant = Merchant.objects.get(owner=user)
        except Merchant.DoesNotExist:
            raise MerchantDoesNotExist

        if not Hashtag.objects.filter(name=hashtag_info.name):
            Hashtag.objects.create(
                name=hashtag_info.name,
            )
