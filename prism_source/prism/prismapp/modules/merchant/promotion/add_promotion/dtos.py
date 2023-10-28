from dataclasses import dataclass
from datetime import datetime


@dataclass
class PromotionInformation:
    name: str
    quantity: int
    unit: str
    description: str
    images: dict
    total_bookings: int
    start_date: datetime
    end_date: datetime
    discount: float
    type: str
    buy_quantity: int
    get_quantity: int
    products: list[str]
    services: list[str]
    all_day: bool
    is_happy_hour: bool
