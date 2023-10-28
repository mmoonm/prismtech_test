from django.urls import path, include
from prismapp.modules.merchant.collection.add_collection.view import AddCollectionView
from prismapp.modules.merchant.collection.remove_collection.view import RemoveCollectionView

urlpatterns = [
    path('add-collection/', AddCollectionView.as_view()),
    path('remove-collection/', RemoveCollectionView.as_view()),
]
