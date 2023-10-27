from rest_framework import serializers


class StringListField(serializers.ListField):
    child = serializers.CharField(allow_blank=True, allow_null=True)


class InputSerializer(serializers.Serializer):

    name = serializers.CharField(max_length=255, allow_blank=False, allow_null=False)
    description = serializers.CharField(allow_blank=True, allow_null=True)
    description_html = serializers.CharField(allow_blank=True, allow_null=True)
    email = serializers.CharField(max_length=255, allow_blank=True, allow_null=True)
    phone_number = serializers.CharField(max_length=45, allow_blank=True, allow_null=True)
    country_code = serializers.CharField(max_length=4, allow_blank=True, allow_null=True)
    country_number = serializers.CharField(max_length=4, allow_blank=True, allow_null=True)
    platform_number = serializers.CharField(max_length=45, allow_blank=True, allow_null=True)
    website = serializers.CharField(max_length=255, allow_blank=True, allow_null=True)
    latitude = serializers.DecimalField(max_digits=12, decimal_places=9, allow_null=True)
    longitude = serializers.DecimalField(max_digits=12, decimal_places=9, allow_null=True)
    address = serializers.CharField(max_length=255, allow_blank=True, allow_null=True)
    is_active = serializers.BooleanField(default=True)
    hashtags = StringListField()
    categories = StringListField()
    keywords = StringListField()
    is_staffs_visible = serializers.BooleanField(default=True)
    total_available_slot = serializers.IntegerField(default=0, allow_null=True)
    total_available_slots_unit = serializers.CharField(max_length=45, allow_null=True)
    total_bookings = serializers.IntegerField(default=0, allow_null=True)
    banner = serializers.JSONField(default=dict, allow_null=True)
    allow_staff_connect_user = serializers.BooleanField(default=False)
    note_placeholder = serializers.CharField(max_length=255, allow_null=True, allow_blank=True)
