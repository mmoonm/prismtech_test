__all__=[
    "MerchantDoesNotExist",
    "CategoryDoesNotExist",
    "HashtagDoesNotExist"
]


class MerchantDoesNotExist(Exception):
    pass

class CategoryDoesNotExist(Exception):
    pass

class HashtagDoesNotExist(Exception):
    pass
