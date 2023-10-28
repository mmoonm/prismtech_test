__all__ = ["RemoveCollectionView"]

import logging
import traceback
from rest_framework.permissions import IsAuthenticated
from rest_framework.request import Request
from prismapp.common.base_view import BaseAPIView
from prismapp.modules.merchant.collection.remove_collection.dtos import CollectionInformation
from prismapp.modules.merchant.collection.remove_collection.serializers import InputSerializer
from prismapp.modules.merchant.collection.remove_collection.service import RemoveCollectionService
from prismapp.modules.merchant.collection.remove_collection.exceptions import MerchantDoesNotExist, CollectionDoesNotExist


class RemoveCollectionView(BaseAPIView):
    permission_classes = [IsAuthenticated]

    class ResponseCode:
        SUCCESS = "SUCCESS"
        INVALID_PARAMS = 'INVALID PARAMS'
        MERCHANTDOESNOTEXIST = "MERCHANT DOES NOT EXIST"
        COLLECTIONDOESNOTEXIST = "COLLECTION DOES NOT EXIST"

    def __init__(self):
        super().__init__()
        self.service = RemoveCollectionService()

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

        collection_info = CollectionInformation(
            name=input_data.validated_data.get('name'),
        )

        try:
            self.service.remove_collection(request.user, collection_info)
            return self._build_response(success=True, response_code=self.ResponseCode.SUCCESS)
        except MerchantDoesNotExist:
            return self._build_response(success=False, response_code=self.ResponseCode.MERCHANTDOESNOTEXIST)
        except CollectionDoesNotExist:
            return self._build_response(success=False, response_code=self.ResponseCode.COLLECTIONDOESNOTEXIST)
