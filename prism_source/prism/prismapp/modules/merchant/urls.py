from django.urls import path, include
from prismapp.modules.merchant.create_merchant.view import CreateMerchant
from prismapp.modules.merchant.product import urls as producturls
from prismapp.modules.merchant.service import urls as serviceurls
from prismapp.modules.merchant.promotion import urls as promotionurls
from prismapp.modules.merchant.category import urls as categoryurls
from prismapp.modules.merchant.keyword import urls as keywordurls
from prismapp.modules.merchant.hashtag import urls as hashtagurls
from prismapp.modules.merchant.collection import urls as collectionurls

urlpatterns = [
    path('create-merchant/', CreateMerchant.as_view()),
    path('product/', include(producturls)),
    path('service/', include(serviceurls)),
    path('promotion/', include(promotionurls)),
    path('category/', include(categoryurls)),
    path('keyword/', include(keywordurls)),
    path('hashtag/', include(hashtagurls)),
    path('collection/', include(collectionurls)),
]
