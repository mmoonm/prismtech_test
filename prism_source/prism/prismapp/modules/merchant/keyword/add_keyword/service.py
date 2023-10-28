__all__ = ['AddKeywordService']

from prismapp.models import Merchant, Hashtag, Keyword
from prismapp.modules.merchant.keyword.add_keyword.dtos import KeywordInformation
from prismapp.modules.merchant.keyword.add_keyword.exceptions import MerchantDoesNotExist


class AddKeywordService:

    def add_keyword(self, user, keyword_info: KeywordInformation):

        try:
            merchant = Merchant.objects.get(owner=user)
        except Merchant.DoesNotExist:
            raise MerchantDoesNotExist

        if not Keyword.objects.filter(name=keyword_info.name):
            Keyword.objects.create(
                name=keyword_info.name,
            )
