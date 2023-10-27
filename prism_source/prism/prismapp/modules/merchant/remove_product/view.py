__all__ = ["RemoveProduct"]
from rest_framework.request import Request
from prismapp.common.base_view import BaseAPIView


class RemoveProduct(BaseAPIView):
    def __init__(self):
        super().__init__()

    def get(self, request: Request):
        return self._build_response(success=True, data="Remove product")
