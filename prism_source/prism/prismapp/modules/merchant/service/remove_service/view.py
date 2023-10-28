__all__ = ["RemoveServiceView"]

import logging
import traceback
from rest_framework.permissions import IsAuthenticated
from rest_framework.request import Request
from prismapp.common.base_view import BaseAPIView
from prismapp.modules.merchant.service.remove_service.dtos import ServiceInformation
from prismapp.modules.merchant.service.remove_service.serializers import InputSerializer
from prismapp.modules.merchant.service.remove_service.service import RemoveServiceService
from prismapp.modules.merchant.service.remove_service.exceptions import MerchantDoesNotExist


class RemoveServiceView(BaseAPIView):
    permission_classes = [IsAuthenticated]

    class ResponseCode:
        SUCCESS = "SUCCESS"
        INVALID_PARAMS = 'INVALID PARAMS'
        MERCHANTDOESNOTEXIST = "MERCHANT DOES NOT EXIST"

    def __init__(self):
        super().__init__()
        self.service = RemoveServiceService()

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
            name=input_data.validated_data.get('name')
        )

        try:
            self.service.remove_service(request.user, service_info)
            return self._build_response(success=True, response_code=self.ResponseCode.SUCCESS)
        except MerchantDoesNotExist:
            return self._build_response(success=False, response_code=self.ResponseCode.MERCHANTDOESNOTEXIST)
