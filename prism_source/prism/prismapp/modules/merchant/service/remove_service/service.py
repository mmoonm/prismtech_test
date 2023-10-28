__all__ = ['RemoveServiceService']

from prismapp.models import Merchant, Service, Hashtag, Keyword
from prismapp.modules.merchant.service.remove_service.dtos import ServiceInformation
from prismapp.modules.merchant.service.remove_service.exceptions import MerchantDoesNotExist


class RemoveServiceService:

    def remove_service(self, user, service_info: ServiceInformation):

        try:
            merchant = Merchant.objects.get(owner=user)
        except Merchant.DoesNotExist:
            raise MerchantDoesNotExist

        service = Service.objects.filter(
            owner=user,
            merchant=merchant,
            name=service_info.name
        )

        if service is not None:
            service.delete()