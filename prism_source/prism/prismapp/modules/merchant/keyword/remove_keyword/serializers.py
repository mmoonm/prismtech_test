from rest_framework import serializers


class InputSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=50, allow_null=False)
