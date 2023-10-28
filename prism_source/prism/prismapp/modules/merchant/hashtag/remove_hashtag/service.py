__all__ = ['RemoveHashtagService']

from prismapp.models import Merchant, Hashtag
from prismapp.modules.merchant.hashtag.remove_hashtag.dtos import HashtagInformation
from prismapp.modules.merchant.hashtag.remove_hashtag.exceptions import MerchantDoesNotExist, HashtagDoesNotExist

class RemoveHashtagService:

    def remove_hashtag(self, user, hashtag_info: HashtagInformation):

        try:
            merchant = Merchant.objects.get(owner=user)
        except Merchant.DoesNotExist:
            raise MerchantDoesNotExist

        try:
            hashtag = Hashtag.objects.get(
                name=hashtag_info.name
            )
        except Hashtag.DoesNotExist:
            raise HashtagDoesNotExist

        if hashtag is not None:
            hashtag.delete()
