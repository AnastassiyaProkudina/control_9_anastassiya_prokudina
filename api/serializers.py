from rest_framework import serializers

from accounts.models import Account
from gallery.models import Favorites


# class PhotoSerializer(serializers.ModelSerializer):
#
#
#     class Meta:
#         model = Photo
#         fields = ['id', 'photo', 'author', 'created_at', 'updated_at']
#         read_only_fields = ['id', 'author', 'created_ad', 'updates_at']
#
#     def create(self, validated_data, author=None):
#         return Photo.objects.create(**validated_data, author=self.author)
#
#     def update(self, instance, validated_data):
#         instance.text = validated_data.get('text')
#         instance.image = validated_data.get('photo', instance.photo)
#         instance.save()
#         return instance


class AccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = ('id', 'username')
        read_only_fields = ('username',)


class FavoriteSerializer(serializers.ModelSerializer):
    photo_caption = serializers.CharField(read_only=True, source='photo.caption')
    photo_photo = serializers.ImageField(read_only=True, source='photo.photo')
    author = AccountSerializer(read_only=True)

    class Meta:
        model = Favorites
        fields = ('id', 'author', 'photo', 'photo_caption', 'photo_photo')
        read_only_fields = ('id', 'author', 'photo_caption', 'photo_photo')

    def create(self, validated_data, account=None):
        return Favorites.objects.create(**validated_data, author=self.author)

