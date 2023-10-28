__all__ = ['AddService']

from prismapp.models import Merchant, Category, Hashtag, Keyword, Service
from prismapp.modules.merchant.service.add_service.dtos import ServiceInformation
from prismapp.modules.merchant.service.add_service.exceptions import MerchantDoesNotExist


class AddService:

    def add_service(self, user, service_info: ServiceInformation):

        try:
            merchant = Merchant.objects.get(owner=user)
        except Merchant.DoesNotExist:
            raise MerchantDoesNotExist

        service = Service.objects.create(
            owner=user,
            merchant=merchant,
            name=service_info.name,
            time=service_info.time,
            available_slots=service_info.available_slots,
            slots_unit=service_info.slots_unit,
            description=service_info.description,
            description_html=service_info.description_html,
            original_price=service_info.original_price,
            discount_price=service_info.discount_price,
            images=service_info.images,
            total_bookings=service_info.total_bookings,
            hidden=service_info.hidden,
            sold_quantity=service_info.sold_quantity
            # ...
        )

        if service_info.hashtags is not None:
            for hashtag in service_info.hashtags:
                if not Hashtag.objects.filter(name=hashtag).exists():
                    Hashtag.objects.create(name=hashtag)

                service.hashtags.add(Hashtag.objects.get(name=hashtag))

        if service_info.keywords is not None:
            for keyword in service_info.keywords:
                if not Keyword.objects.filter(name=keyword).exists():
                    Keyword.objects.create(name=keyword)
                service.keywords.add(Keyword.objects.get(name=keyword))

