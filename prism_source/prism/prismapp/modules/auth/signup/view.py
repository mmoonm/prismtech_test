from django.contrib.auth.hashers import make_password
from django.http import JsonResponse
from rest_framework import serializers, status

from prismapp.common.base_view import BaseAPIView
from prismapp.models import User


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('email', 'password')
        extra_kwargs = {'password': {'write_only': True}}


class UserRegisterView(BaseAPIView):

    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.validated_data['password'] = make_password(serializer.validated_data['password'])
            user = serializer.save()

            return JsonResponse({
                'message': 'Register successful!'
            }, status=status.HTTP_201_CREATED)

        else:
            return JsonResponse({
                'error_message': 'This email has already exist!',
                'errors_code': 400,
            }, status=status.HTTP_400_BAD_REQUEST)
