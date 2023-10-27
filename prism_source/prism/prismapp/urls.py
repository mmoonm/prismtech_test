from django.urls import path, include
from prismapp.modules.merchant import urls as merchanturls
from prismapp.modules.auth import urls as authurls


urlpatterns = [
    path('merchant/', include(merchanturls)),
    path('auth/', include(authurls)),
]
