__all__ = ["CreateMerchant"]

import logging
import traceback
from rest_framework import serializers
from rest_framework.permissions import IsAuthenticated
from rest_framework.request import Request
from prismapp.common.base_view import BaseAPIView
from prismapp.modules.merchant.create_merchant.dtos import MerchantInformation
from prismapp.modules.merchant.create_merchant.serializers import InputSerializer
from prismapp.modules.merchant.create_merchant.service import CreateMerchantService
from dacite import from_dict


class CreateMerchant(BaseAPIView):
    permission_classes = [IsAuthenticated]

    class ResponseCode:
        SUCCESS = "SUCCESS"
        INVALID_PARAMS = 'INVALID PARAMS'
        USER_HAD_A_MERCHANT = 'USER HAD A MERCHANT ALREADY'

    def __init__(self):
        super().__init__()
        self.service = CreateMerchantService()

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
        merchant_info = from_dict(data_class=MerchantInformation, data=dict(input_data.validated_data))
        a = self.service.create_merchant(user=request.user, merchant_info=merchant_info)

        return self._build_response(success=True, data="CreateMerchant")
