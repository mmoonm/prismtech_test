from django.urls import path, include
from prismapp.modules.merchant import urls as merchanturls

urlpatterns = [
    path('merchant/', include(merchanturls)),
]
