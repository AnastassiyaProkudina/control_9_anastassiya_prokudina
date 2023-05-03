from rest_framework import status
from rest_framework.generics import get_object_or_404
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from api.serializers import CommentSerializer
from gallery.models import Photo, Comment


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


class CommentView(APIView):
    permission_classes = [IsAuthenticated]
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

    def post(self, request, *args, **kwargs):
        CommentSerializer.author = request.user
        CommentSerializer.photo = get_object_or_404(Photo, pk=kwargs.get('pk'))
        serializer = CommentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CommentDeleteView(APIView):
    permission_classes = [IsAuthenticated]
    queryset = Comment.objects.all()

    def delete(self, request, *args, **kwargs):
        comment = get_object_or_404(Comment, pk=kwargs.get('pk'))
        comment.delete()
        return Response({"success": True}, status=status.HTTP_200_OK)
