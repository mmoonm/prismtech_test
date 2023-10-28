from rest_framework import serializers


class StringListField(serializers.ListField):
    child = serializers.CharField(allow_blank=True, allow_null=True, default=None)


class InputSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=255, allow_null=False)
