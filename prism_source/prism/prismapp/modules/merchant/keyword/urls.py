from django.urls import path, include
from prismapp.modules.merchant.keyword.add_keyword.view import AddKeywordView
from prismapp.modules.merchant.keyword.remove_keyword.view import RemoveKeywordView

urlpatterns = [
    path('add-keyword/', AddKeywordView.as_view()),
    path('remove-keyword/', RemoveKeywordView.as_view()),
]
