from dataclasses import dataclass


@dataclass
class ProductInformation:
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
