__all__ = ["RemoveCategoryView"]

import logging
import traceback
from rest_framework.permissions import IsAuthenticated
from rest_framework.request import Request
from prismapp.common.base_view import BaseAPIView
from prismapp.modules.merchant.category.remove_category.dtos import CategoryInformation
from prismapp.modules.merchant.category.remove_category.serializers import InputSerializer
from prismapp.modules.merchant.category.remove_category.service import RemoveCategoryService
from prismapp.modules.merchant.category.remove_category.exceptions import MerchantDoesNotExist, CategoryDoesNotExist, \
    HashtagDoesNotExist


class RemoveCategoryView(BaseAPIView):
    permission_classes = [IsAuthenticated]

    class ResponseCode:
        SUCCESS = "SUCCESS"
        INVALID_PARAMS = 'INVALID PARAMS'
        MERCHANTDOESNOTEXIST = "MERCHANT DOES NOT EXIST"
        CATEGORYDOESNOTEXIST = "CATEGORY DOES NOT EXIST"
        HASHTAGDOESNOTEXIST = "HASHTAG DOES NOT EXIST"

    def __init__(self):
        super().__init__()
        self.service = RemoveCategoryService()

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
            hashtag=input_data.validated_data.get('hashtag'),
        )

        try:
            self.service.remove_category(request.user, category_info)
            return self._build_response(success=True, response_code=self.ResponseCode.SUCCESS)
        except MerchantDoesNotExist:
            return self._build_response(success=False, response_code=self.ResponseCode.MERCHANTDOESNOTEXIST)
        except CategoryDoesNotExist:
            return self._build_response(success=False, response_code=self.ResponseCode.CATEGORYDOESNOTEXIST)
        except HashtagDoesNotExist:
            return self._build_response(success=False, response_code=self.ResponseCode.HASHTAGDOESNOTEXIST)
