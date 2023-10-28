from dataclasses import dataclass


@dataclass
class ServiceInformation:
    name: str
    hashtags: list[str]
    keywords: list[str]
    categories: str
    quantity: int
    unit: str
    description: str
    description_html: str
    original_price: float
    discount_price: float
    images: dict
    total_bookings: int
    hidden: bool
    sold_quantity: int

    time: float
    time_date: str
    require_staff: bool
    available_slots: int
    slots_unit: str
    use_total_available_slots: bool
    flexible_time: bool
