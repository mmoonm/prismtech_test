__all__ = ['AbstractAPIView']
from rest_framework.views import APIView


class AbstractAPIView(APIView):

    @staticmethod
    def _build_response(success, data=None, errors=None, messages=None, response_code=None, http_status=200, *args, **kwargs):
        response_data = {'success': success}

        if data is not None:
            response_data['data'] = data

        if errors is not None:
            response_data['errors'] = errors

        if messages is not None:
            response_data['messages'] = messages

        if response_code is not None:
            response_data['response_code'] = response_code

        if http_status is not None:
            response_data['http_status'] = http_status

        return response_data
