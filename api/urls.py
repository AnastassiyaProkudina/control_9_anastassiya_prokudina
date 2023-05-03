from django.urls import path

from api.views import FavoriteView, CommentView, CommentDeleteView

urlpatterns = [
    path("favorites/photo/<int:id>", FavoriteView.as_view(), name="favorite"),
    path("comment/create/photo/<int:pk>", CommentView.as_view(), name="comment_create"),
    path("comment/<int:pk>/delete/", CommentDeleteView.as_view(), name="comment_delete"),
]
