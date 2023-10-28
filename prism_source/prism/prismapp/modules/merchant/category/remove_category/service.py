__all__ = ['RemoveCategoryService']

from prismapp.models import Merchant, Category, Hashtag, Keyword
from prismapp.modules.merchant.category.remove_category.dtos import CategoryInformation
from prismapp.modules.merchant.category.remove_category.exceptions import MerchantDoesNotExist, CategoryDoesNotExist, \
    HashtagDoesNotExist


class RemoveCategoryService:

    def remove_category(self, user, category_info: CategoryInformation):

        try:
            merchant = Merchant.objects.get(owner=user)
        except Merchant.DoesNotExist:
            raise MerchantDoesNotExist

        try:
            hashtag = Hashtag.objects.get(name=category_info.hashtag)
        except Hashtag.DoesNotExist:
            raise HashtagDoesNotExist

        try:
            category = Category.objects.get(
                owner=user,
                name_vi=category_info.name_vi,
                name_en=category_info.name_en,
                hashtag=hashtag,
            )
        except Category.DoesNotExist:
            raise CategoryDoesNotExist

        if category is not None:
            category.delete()
