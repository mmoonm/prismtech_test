from rest_framework import serializers


class InputSerializer(serializers.Serializer):
    name_vi = serializers.CharField(max_length=50, default="SOME STRING")
    name_en = serializers.CharField(max_length=50, default="SOME STRING")
    notes = serializers.CharField(max_length=200)
    hashtag = serializers.CharField(max_length=200)
    image = serializers.CharField(default=None, allow_null=True, allow_blank=True, max_length=1000)
