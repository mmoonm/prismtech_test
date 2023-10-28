from rest_framework import serializers


class StringListField(serializers.ListField):
    child = serializers.CharField(allow_blank=True, allow_null=True, default=None)


class InputSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=255, allow_null=False)
    quantity = serializers.IntegerField(default=0)
    unit = serializers.CharField(max_length=255, allow_null=True, default=None)
    description = serializers.CharField(allow_null=True, allow_blank=True)
    images = serializers.JSONField(default=dict, allow_null=True)
    total_bookings = serializers.IntegerField(default=0, allow_null=True)
    start_date = serializers.DateTimeField(allow_null=True)
    end_date = serializers.DateTimeField(allow_null=True)
    discount = serializers.FloatField(allow_null=True, default=None)
    type = serializers.CharField(max_length=255, allow_null=True, allow_blank=True, default="discount")
    buy_quantity = serializers.IntegerField(allow_null=True)
    get_quantity = serializers.IntegerField(allow_null=True)
    products = StringListField(default=None)
    services = StringListField(default=None)
    all_day = serializers.BooleanField(default=False)
    is_happy_hour = serializers.BooleanField(default=False)
