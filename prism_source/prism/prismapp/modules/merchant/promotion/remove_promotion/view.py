__all__ = ["RemovePromotionView"]

import logging
import traceback
from rest_framework.permissions import IsAuthenticated
from rest_framework.request import Request
from prismapp.common.base_view import BaseAPIView
from prismapp.modules.merchant.promotion.remove_promotion.dtos import PromotionInformation
from prismapp.modules.merchant.promotion.remove_promotion.serializers import InputSerializer
from prismapp.modules.merchant.promotion.remove_promotion.service import RemovePromotionService
from prismapp.modules.merchant.promotion.remove_promotion.exceptions import MerchantDoesNotExist


class RemovePromotionView(BaseAPIView):
    permission_classes = [IsAuthenticated]

    class ResponseCode:
        SUCCESS = "SUCCESS"
        INVALID_PARAMS = 'INVALID PARAMS'
        MERCHANTDOESNOTEXIST = "MERCHANT DOES NOT EXIST"

    def __init__(self):
        super().__init__()
        self.service = RemovePromotionService()

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
            name=input_data.validated_data.get('name')
        )

        try:
            self.service.remove_promotion(request.user, promotion_info)
            return self._build_response(success=True, response_code=self.ResponseCode.SUCCESS)
        except MerchantDoesNotExist:
            return self._build_response(success=False, response_code=self.ResponseCode.MERCHANTDOESNOTEXIST)
