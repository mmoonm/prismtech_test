__all__ = ['RemoveKeywordService']

from prismapp.models import Merchant, Hashtag, Keyword
from prismapp.modules.merchant.keyword.remove_keyword.dtos import KeywordInformation
from prismapp.modules.merchant.keyword.remove_keyword.exceptions import MerchantDoesNotExist, KeywordDoesNotExist

class RemoveKeywordService:

    def remove_keyword(self, user, keyword_info: KeywordInformation):

        try:
            merchant = Merchant.objects.get(owner=user)
        except Merchant.DoesNotExist:
            raise MerchantDoesNotExist


        try:
            keyword = Keyword.objects.get(
                name=keyword_info.name
            )
        except Keyword.DoesNotExist:
            raise KeywordDoesNotExist

        if keyword is not None:
            keyword.delete()
