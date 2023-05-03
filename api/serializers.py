from rest_framework import serializers

from accounts.models import Account
from gallery.models import Comment


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ['id', 'text', 'photo', 'author',  'created_at']
        read_only_fields = ['id', 'photo', 'author', 'created_ad']

    def create(self, validated_data, author=None, photo=None):
        comment = Comment.objects.create(**validated_data, author=self.author, photo=self.photo)
        return comment

