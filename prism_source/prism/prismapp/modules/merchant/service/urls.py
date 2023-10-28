from django.urls import path, include
from prismapp.modules.merchant.service.add_service.view import AddServiceView
from prismapp.modules.merchant.service.remove_service.view import RemoveServiceView

urlpatterns = [
    path('add-service/', AddServiceView.as_view()),
    path('remove-service/', RemoveServiceView.as_view()),
]
