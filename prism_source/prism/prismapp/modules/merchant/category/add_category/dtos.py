from dataclasses import dataclass


@dataclass
class CategoryInformation:
    name_vi: str
    name_en: str
    notes: str
    hashtag: str
    image: str
