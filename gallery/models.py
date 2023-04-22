from django.contrib.auth import get_user_model
from django.contrib.auth.models import User
from django.db import models

import accounts


class Photo(models.Model):
    photo = models.ImageField(
        verbose_name="Фото", null=False, blank=False, upload_to="user_pic"
    )
    caption = models.CharField(
        verbose_name="Подпись", null=False, max_length=1000, blank=False
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name="Время создания",
    )
    author = models.ForeignKey(
        verbose_name="Автор",
        to=get_user_model(),
        related_name="photos",
        on_delete=models.CASCADE,
    )
    updated_at = models.DateTimeField(
        auto_now=True, verbose_name="Date and time updated"
    )
    is_deleted = models.BooleanField(verbose_name="Deleted", null=False, default=False)
    deleted_at = models.DateTimeField(
        verbose_name="Date and time deleted at", null=True, default=None
    )


class Favorites(models.Model):
    author = models.ForeignKey(
        verbose_name="Автор",
        to=get_user_model(),
        related_name="favorite",
        on_delete=models.CASCADE,
    )
    photo = models.ForeignKey(
        verbose_name="Публикация",
        to="gallery.Photo",
        related_name="favorite",
        on_delete=models.CASCADE,
    )



