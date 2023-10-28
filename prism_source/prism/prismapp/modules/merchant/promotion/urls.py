from django.urls import path, include

from prismapp.modules.merchant.promotion.add_promotion.view import AddPromotionView
from prismapp.modules.merchant.promotion.remove_promotion.view import RemovePromotionView

urlpatterns = [
    path('add-promotion/', AddPromotionView.as_view()),
    path('remove-promotion/', RemovePromotionView.as_view()),
]
