from rest_framework import serializers


class StringListField(serializers.ListField):
    child = serializers.CharField(allow_blank=True, allow_null=True, default=None)


class InputSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=255, allow_null=False)
    hashtags = StringListField(default=None)
    keywords = StringListField(default=None)
    quantity = serializers.IntegerField(default=0)
    unit = serializers.CharField(max_length=255, allow_null=True, default=None)
    description = serializers.CharField(allow_null=True, allow_blank=True)
    description_html = serializers.CharField(allow_null=True, allow_blank=True)
    original_price = serializers.DecimalField(max_digits=12, decimal_places=2, default=0.0, allow_null=True)
    discount_price = serializers.DecimalField(max_digits=12, decimal_places=2, default=0.0, allow_null=True)
    images = serializers.JSONField(default=dict, allow_null=True)
    total_bookings = serializers.IntegerField(default=0, allow_null=True)
    hidden = serializers.BooleanField(default=False)
    sold_quantity = serializers.IntegerField(default=0, help_text="Product sold quantity")
