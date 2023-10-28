__all__ = ['AddCollectionService']

from prismapp.models import Merchant, Collection
from prismapp.modules.merchant.collection.add_collection.dtos import CollectionInformation
from prismapp.modules.merchant.collection.add_collection.exceptions import MerchantDoesNotExist


class AddCollectionService:

    def add_collection(self, user, collection_info: CollectionInformation):

        try:
            merchant = Merchant.objects.get(owner=user)
        except Merchant.DoesNotExist:
            raise MerchantDoesNotExist

        if not Collection.objects.filter(name=collection_info.name):
            Collection.objects.create(
                name=collection_info.name,
                merchant=merchant,
                owner=user
            )
