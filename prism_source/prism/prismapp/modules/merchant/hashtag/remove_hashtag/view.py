__all__ = ["RemoveHashtagView"]

import logging
import traceback
from rest_framework.permissions import IsAuthenticated
from rest_framework.request import Request
from prismapp.common.base_view import BaseAPIView
from prismapp.modules.merchant.hashtag.remove_hashtag.dtos import HashtagInformation
from prismapp.modules.merchant.hashtag.remove_hashtag.serializers import InputSerializer
from prismapp.modules.merchant.hashtag.remove_hashtag.service import RemoveHashtagService
from prismapp.modules.merchant.hashtag.remove_hashtag.exceptions import MerchantDoesNotExist, HashtagDoesNotExist


class RemoveHashtagView(BaseAPIView):
    permission_classes = [IsAuthenticated]

    class ResponseCode:
        SUCCESS = "SUCCESS"
        INVALID_PARAMS = 'INVALID PARAMS'
        MERCHANTDOESNOTEXIST = "MERCHANT DOES NOT EXIST"
        HASHTAGDOESNOTEXIST = "HASHTAG DOES NOT EXIST"

    def __init__(self):
        super().__init__()
        self.service = RemoveHashtagService()

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

        hashtag_info = HashtagInformation(
            name=input_data.validated_data.get('name'),
        )

        try:
            self.service.remove_hashtag(request.user, hashtag_info)
            return self._build_response(success=True, response_code=self.ResponseCode.SUCCESS)
        except MerchantDoesNotExist:
            return self._build_response(success=False, response_code=self.ResponseCode.MERCHANTDOESNOTEXIST)
        except HashtagDoesNotExist:
            return self._build_response(success=False, response_code=self.ResponseCode.HASHTAGDOESNOTEXIST)
