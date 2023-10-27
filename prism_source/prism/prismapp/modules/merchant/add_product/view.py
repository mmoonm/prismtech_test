__all__ = ["AddProduct"]
from rest_framework.request import Request
from rest_framework.response import Response

from prismapp.common.base_view import BaseAPIView

class AddProduct(BaseAPIView):
    def __init__(self):
        super().__init__()

    def get(self, request: Request):
        return self._build_response(success=True, data="HAHAHAHAHAHA")
