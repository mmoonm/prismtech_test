from django.urls import path, include
from prismapp.modules.merchant.hashtag.add_hashtag.view import AddHashtagView
from prismapp.modules.merchant.hashtag.remove_hashtag.view import RemoveHashtagView

urlpatterns = [
    path('add-hashtag/', AddHashtagView.as_view()),
    path('remove-hashtag/', RemoveHashtagView.as_view()),
]
