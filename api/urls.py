from django.urls import path

from api.views import FavoriteView


urlpatterns = [
    path("favorites/photo/<int:id>", FavoriteView.as_view(), name="favorite"),
]
