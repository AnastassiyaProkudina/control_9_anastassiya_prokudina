from django.contrib.auth import get_user_model
from django.contrib.auth.models import User
from django.db import models

import accounts


class Photo(models.Model):
    photo = models.ImageField(
        verbose_name="Фото", null=False, blank=False, upload_to="photos"
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
    user_favorites = models.ManyToManyField(
        verbose_name="Избранные фотографии",
        to=get_user_model(),
        related_name="user_favorites",
    )


class Comment(models.Model):
    text = models.TextField(
        verbose_name="Комментарий", null=False, blank=False, max_length=200
    )
    photo = models.ForeignKey(
        verbose_name="Публикация",
        to="Photo",
        related_name="comments",
        on_delete=models.CASCADE,
        blank=False
    )
    author = models.ForeignKey(
        verbose_name="Автор",
        to=get_user_model(),
        related_name="comments",
        on_delete=models.CASCADE,
        blank=False
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name="Дата и время создания",
    )

    def __str__(self):
        return self.text[:20]
