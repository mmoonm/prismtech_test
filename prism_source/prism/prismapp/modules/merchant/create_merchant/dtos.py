from dataclasses import dataclass


@dataclass
class MerchantInformation:
    name: str
    description: str
    description_html: str
    email: str
    phone_number: str
    country_code: str
    country_number: str
    platform_number: str
    website: str
    latitude: float
    longitude: float
    address: str
    is_active: bool
    hashtags: list[str]
    categories: list[str]
    keywords: list[str]
    is_staffs_visible: bool
    total_available_slot: int
    total_available_slots_unit: str
    total_bookings: int
    banner: dict
    allow_staff_connect_user: bool
    note_placeholder: str
