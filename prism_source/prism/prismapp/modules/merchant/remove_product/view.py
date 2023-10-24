__all__ = ["RemoveProduct"]
from rest_framework.request import Request
from rest_framework.response import Response

from prismapp.common.base_view import AbstractAPIView

class RemoveProduct(AbstractAPIView):
    def __init__(self):
        super().__init__()

    def get(self, request: Request):
        return Response(self._build_response(success=True, data="Remove product"))
