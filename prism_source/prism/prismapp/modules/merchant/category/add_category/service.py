__all__ = ['AddCategoryService']

from prismapp.models import Merchant, Category, Category, Hashtag, Keyword
from prismapp.modules.merchant.category.add_category.dtos import CategoryInformation
from prismapp.modules.merchant.category.add_category.exceptions import MerchantDoesNotExist


class AddCategoryService:

    def add_category(self, user, category_info: CategoryInformation):

        try:
            merchant = Merchant.objects.get(owner=user)
        except Merchant.DoesNotExist:
            raise MerchantDoesNotExist

        if category_info.hashtag is not None:
            if not Hashtag.objects.filter(name=category_info.hashtag).exists():
                Hashtag.objects.create(name=category_info.hashtag)

            hashtag = Hashtag.objects.get(name=category_info.hashtag)

        category = Category.objects.create(
            owner=user,
            name_vi=category_info.name_vi,
            name_en=category_info.name_en,
            notes=category_info.notes,
            hashtag=hashtag,
            image=category_info.image
        )



