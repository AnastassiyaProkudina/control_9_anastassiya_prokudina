from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from api.permissions import FavoritePermissions
from api.serializers import FavoriteSerializer
from gallery.models import Favorites


class FavoriteView(ModelViewSet):
    permission_classes = [IsAuthenticated, FavoritePermissions]
    queryset = Favorites.objects.all()
    serializer_class = FavoriteSerializer

    def create(self, request, *args, **kwargs):
        self.serializer_class.author = request.user
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


