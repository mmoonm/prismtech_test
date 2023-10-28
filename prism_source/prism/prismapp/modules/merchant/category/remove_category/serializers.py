from rest_framework import serializers


class InputSerializer(serializers.Serializer):
    name_vi = serializers.CharField(max_length=50, allow_null=False)
    name_en = serializers.CharField(max_length=50, allow_null=False)
    hashtag = serializers.CharField(max_length=200, allow_null=False)
