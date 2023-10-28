__all__ = ["AddCategoryView"]

import logging
import traceback
from rest_framework.permissions import IsAuthenticated
from rest_framework.request import Request
from prismapp.common.base_view import BaseAPIView
from prismapp.modules.merchant.category.add_category.dtos import CategoryInformation
from prismapp.modules.merchant.category.add_category.serializers import InputSerializer
from prismapp.modules.merchant.category.add_category.service import AddCategoryService
from prismapp.modules.merchant.category.add_category.exceptions import MerchantDoesNotExist


class AddCategoryView(BaseAPIView):
    permission_classes = [IsAuthenticated]

    class ResponseCode:
        SUCCESS = "SUCCESS"
        INVALID_PARAMS = 'INVALID PARAMS'
        MERCHANTDOESNOTEXIST = "MERCHANT DOES NOT EXIST"

    def __init__(self):
        super().__init__()
        self.service = AddCategoryService()

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

        category_info = CategoryInformation(
            name_vi=input_data.validated_data.get('name_vi'),
            name_en=input_data.validated_data.get('name_en'),
            notes=input_data.validated_data.get('notes'),
            hashtag=input_data.validated_data.get('hashtag'),
            image=input_data.validated_data.get('image'),
        )

        try:
            self.service.add_category(request.user, category_info)
            return self._build_response(success=True, response_code=self.ResponseCode.SUCCESS)
        except MerchantDoesNotExist:
            return self._build_response(success=False, response_code=self.ResponseCode.MERCHANTDOESNOTEXIST)
