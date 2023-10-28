__all__ = ['RemoveCollectionService']

from prismapp.models import Merchant, Collection
from prismapp.modules.merchant.collection.remove_collection.dtos import CollectionInformation
from prismapp.modules.merchant.collection.remove_collection.exceptions import MerchantDoesNotExist, CollectionDoesNotExist

class RemoveCollectionService:

    def remove_collection(self, user, collection_info: CollectionInformation):

        try:
            merchant = Merchant.objects.get(owner=user)
        except Merchant.DoesNotExist:
            raise MerchantDoesNotExist

        try:
            collection = Collection.objects.get(
                name=collection_info.name,
                merchant=merchant
            )
        except Collection.DoesNotExist:
            raise CollectionDoesNotExist

        if collection is not None:
            collection.delete()
