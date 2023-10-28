__all__ = ["AddPromotionView"]

import logging
import traceback
from rest_framework.permissions import IsAuthenticated
from rest_framework.request import Request
from prismapp.common.base_view import BaseAPIView
from prismapp.modules.merchant.promotion.add_promotion.dtos import PromotionInformation
from prismapp.modules.merchant.promotion.add_promotion.serializers import InputSerializer
from prismapp.modules.merchant.promotion.add_promotion.service import AddPromotionService
from prismapp.modules.merchant.promotion.add_promotion.exceptions import MerchantDoesNotExist


class AddPromotionView(BaseAPIView):
    permission_classes = [IsAuthenticated]

    class ResponseCode:
        SUCCESS = "SUCCESS"
        INVALID_PARAMS = 'INVALID PARAMS'
        MERCHANTDOESNOTEXIST = "MERCHANT DOES NOT EXIST"

    def __init__(self):
        super().__init__()
        self.service = AddPromotionService()

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

        promotion_info = PromotionInformation(
            name=input_data.validated_data.get('name'),
            description=input_data.validated_data.get('description'),
            total_bookings=input_data.validated_data.get('total_bookings', 0),
            quantity=input_data.validated_data.get('quantity', 0),
            unit=input_data.validated_data.get('unit'),
            images=input_data.validated_data.get('images'),
            start_date=input_data.validated_data.get('start_date'),
            end_date=input_data.validated_data.get('end_date'),
            discount=input_data.validated_data.get('discount'),
            type=input_data.validated_data.get('type'),
            buy_quantity=input_data.validated_data.get('buy_quantity'),
            get_quantity=input_data.validated_data.get('get_quantity'),
            products=input_data.validated_data.get('products'),
            services=input_data.validated_data.get('services'),
            all_day=input_data.validated_data.get('all_day'),
            is_happy_hour=input_data.validated_data.get('is_happy_hour')
        )

        try:
            self.service.add_promotion(request.user, promotion_info)
            return self._build_response(success=True, response_code=self.ResponseCode.SUCCESS)
        except MerchantDoesNotExist:
            return self._build_response(success=False, response_code=self.ResponseCode.MERCHANTDOESNOTEXIST)
