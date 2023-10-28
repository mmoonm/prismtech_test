__all__ = ["AddServiceView"]

import logging
import traceback
from rest_framework.permissions import IsAuthenticated
from rest_framework.request import Request
from prismapp.common.base_view import BaseAPIView
from prismapp.modules.merchant.service.add_service.dtos import ServiceInformation
from prismapp.modules.merchant.service.add_service.serializers import InputSerializer
from prismapp.modules.merchant.service.add_service.service import AddService
from prismapp.modules.merchant.service.add_service.exceptions import MerchantDoesNotExist


class AddServiceView(BaseAPIView):
    permission_classes = [IsAuthenticated]

    class ResponseCode:
        SUCCESS = "SUCCESS"
        INVALID_PARAMS = 'INVALID PARAMS'
        MERCHANTDOESNOTEXIST = "MERCHANT DOES NOT EXIST"

    def __init__(self):
        super().__init__()
        self.service = AddService()

    def post(self, request: Request):
        try:
            return self._post(request)
        except Exception as e:
            logging.exception(
                '[x] Uncaught exception: %s' % e.__class__.__name__
            )
            logging.exception('---- Exception message: %s' %e)
            logging.exception(traceback.format_exc())

    def _post(self, request: Request):
        input_data = InputSerializer(data=request.data)
        if input_data.is_valid() is not True:
            return self._build_response(
                success=False,
                response_code=self.ResponseCode.INVALID_PARAMS,
            )

        service_info = ServiceInformation(
            name=input_data.validated_data.get('name'),
            description=input_data.validated_data.get('description'),
            description_html=input_data.validated_data.get('description_html'),
            hashtags=input_data.validated_data.get('hashtags', None),
            categories=input_data.validated_data.get('categories', None),
            keywords=input_data.validated_data.get('keywords', None),
            total_bookings=input_data.validated_data.get('total_bookings', 0),
            quantity=input_data.validated_data.get('quantity', 0),
            unit=input_data.validated_data.get('unit'),
            images=input_data.validated_data.get('images', {}),
            discount_price=input_data.validated_data.get('discount_price'),
            sold_quantity=input_data.validated_data.get('sold_quantity', 0),
            original_price=input_data.validated_data.get('original_price'),
            hidden=input_data.validated_data.get('hidden'),
            time=input_data.validated_data.get('time', 1.0),
            time_date=input_data.validated_data.get('time_date'),
            require_staff=input_data.validated_data.get('require_staff'),
            available_slots=input_data.validated_data.get('available_slots', 1),
            slots_unit=input_data.validated_data.get('slots_unit'),
            use_total_available_slots=input_data.validated_data.get('use_total_available_slots'),
            flexible_time=input_data.validated_data.get('flexible_time'),

        )

        try:
            self.service.add_service(request.user, service_info)
            return self._build_response(success=True, response_code=self.ResponseCode.SUCCESS)
        except MerchantDoesNotExist:
            return self._build_response(success=False, response_code=self.ResponseCode.MERCHANTDOESNOTEXIST)
