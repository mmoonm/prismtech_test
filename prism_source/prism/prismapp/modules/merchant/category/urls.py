from django.urls import path, include
from prismapp.modules.merchant.category.add_category.view import AddCategoryView
from prismapp.modules.merchant.category.remove_category.view import RemoveCategoryView

urlpatterns = [
    path('add-category/', AddCategoryView.as_view()),
    path('remove-category/', RemoveCategoryView.as_view()),
]
