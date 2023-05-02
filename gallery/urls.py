from django.urls import path

from gallery.views.base import IndexView, IndexRedirectView
from gallery.views.photos import *

urlpatterns = [
    path("", IndexView.as_view(), name="index"),
    path("photo/", IndexRedirectView.as_view(), name="photo_index_redirect"),
    path("photo/<int:pk>", PhotoDetail.as_view(), name="photo_detail"),
    path("photo/create", PhotoCreateView.as_view(), name="photo_create"),
    path("photo/<int:pk>/update/", PhotoUpdateView.as_view(), name="photo_update"),
    path("photo/<int:pk>/delete/", PhotoDeleteView.as_view(), name="photo_delete"),
    path(
        "product/<int:pk>/confirm_delete/",
        PhotoDeleteView.as_view(),
        name="photo_confirm_delete",
    ),
]
