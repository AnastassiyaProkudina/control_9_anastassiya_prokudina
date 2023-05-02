from rest_framework import status
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response
from rest_framework.views import APIView

from gallery.models import Photo


class FavoriteView(APIView):
    def put(self, request, id):
        photo = get_object_or_404(Photo, pk=id)
        if request.user not in photo.user_favorites.all():
            photo.user_favorites.add(request.user)
            return Response(
                {"success": True, "favorites": "Yes"}, status=status.HTTP_200_OK
            )
        photo.user_favorites.remove(request.user)
        return Response({"success": True, "favorites": "No"}, status=status.HTTP_200_OK)
