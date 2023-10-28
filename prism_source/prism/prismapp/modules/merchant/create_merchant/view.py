__all__ = ["CreateMerchant"]

import logging
import traceback
from rest_framework import serializers
from rest_framework.permissions import IsAuthenticated
from rest_framework.request import Request
from prismapp.common.base_view import BaseAPIView
from prismapp.modules.merchant.create_merchant.dtos import MerchantInformation
from prismapp.modules.merchant.create_merchant.exceptions import UserAlreadyHasAMerchant
from prismapp.modules.merchant.create_merchant.serializers import InputSerializer
from prismapp.modules.merchant.create_merchant.service import CreateMerchantService


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

        merchant_info = MerchantInformation(
            name=input_data.validated_data.get('name'),
            description=input_data.validated_data.get('description'),
            description_html=input_data.validated_data.get('description_html'),
            email=input_data.validated_data.get('email'),
            phone_number=input_data.validated_data.get('phone_number'),
            country_code=input_data.validated_data.get('country_code'),
            country_number=input_data.validated_data.get('country_number'),
            platform_number=input_data.validated_data.get('platform_number'),
            website=input_data.validated_data.get('website'),
            latitude=input_data.validated_data.get('latitude', 0),
            longitude=input_data.validated_data.get('longitude', 0),
            address=input_data.validated_data.get('address'),
            is_active=input_data.validated_data.get('is_active'),
            hashtags=input_data.validated_data.get('hashtags', None),
            categories=input_data.validated_data.get('categories', None),
            keywords=input_data.validated_data.get('keywords', None),
            is_staffs_visible=input_data.validated_data.get('is_staffs_visible'),
            total_available_slot=input_data.validated_data.get('total_available_slot', 0),
            total_available_slots_unit=input_data.validated_data.get('total_available_slots_unit'),
            total_bookings=input_data.validated_data.get('total_bookings', 0),
            banner=input_data.validated_data.get('banner'),
            allow_staff_connect_user=input_data.validated_data.get('allow_staff_connect_user'),
            note_placeholder=input_data.validated_data.get('note_placeholder'),
        )

        try:
            self.service.create_merchant(user=request.user, merchant_info=merchant_info)
            return self._build_response(success=True, response_code=self.ResponseCode.SUCCESS)
        except UserAlreadyHasAMerchant:
            return self._build_response(success=False, response_code=self.ResponseCode.USER_HAD_A_MERCHANT)
