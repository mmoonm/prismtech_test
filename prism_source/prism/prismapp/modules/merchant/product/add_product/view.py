__all__ = ["AddProduct"]

import logging
import traceback
from rest_framework.permissions import IsAuthenticated
from rest_framework.request import Request
from prismapp.common.base_view import BaseAPIView
from prismapp.modules.merchant.product.add_product.dtos import ProductInformation
from prismapp.modules.merchant.product.add_product.serializers import InputSerializer
from prismapp.modules.merchant.product.add_product.service import AddProductService
from prismapp.modules.merchant.product.add_product.exceptions import MerchantDoesNotExist


class AddProduct(BaseAPIView):
    permission_classes = [IsAuthenticated]

    class ResponseCode:
        SUCCESS = "SUCCESS"
        INVALID_PARAMS = 'INVALID PARAMS'
        MERCHANTDOESNOTEXIST = "MERCHANT DOES NOT EXIST"

    def __init__(self):
        super().__init__()
        self.service = AddProductService()

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

        product_info = ProductInformation(
            name=input_data.validated_data.get('name'),
            description=input_data.validated_data.get('description'),
            description_html=input_data.validated_data.get('description_html'),
            hashtags=input_data.validated_data.get('hashtags', None),
            categories=input_data.validated_data.get('categories', None),
            keywords=input_data.validated_data.get('keywords', None),
            total_bookings=input_data.validated_data.get('total_bookings', 0),
            quantity=input_data.validated_data.get('quantity', 0),
            unit=input_data.validated_data.get('unit'),
            images=input_data.validated_data.get('images'),
            discount_price=input_data.validated_data.get('discount_price'),
            sold_quantity=input_data.validated_data.get('sold_quantity', 0),
            original_price=input_data.validated_data.get('original_price'),
            hidden=input_data.validated_data.get('hidden')
        )

        try:
            self.service.add_product(request.user, product_info)
            return self._build_response(success=True, response_code=self.ResponseCode.SUCCESS)
        except MerchantDoesNotExist:
            return self._build_response(success=False, response_code=self.ResponseCode.MERCHANTDOESNOTEXIST)
