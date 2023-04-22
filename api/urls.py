from django.urls import path, include
from rest_framework import routers

from api.views.favorites import FavoriteView


router = routers.DefaultRouter()
router.register('favorites', FavoriteView)

urlpatterns = [
    path("", include(router.urls)),
]
