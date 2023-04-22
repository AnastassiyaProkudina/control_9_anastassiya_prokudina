from django.contrib.auth.models import User
from django.db import models


class Photo(models.Model):
    image = models.ImageField(
        verbose_name="Фото", null=False, blank=False, upload_to="photos"
    )
    caption = models.CharField(
        verbose_name="Текст", null=False, max_length=1000, blank=False
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name="Время создания",
    )
    author = models.ForeignKey(
        verbose_name="Автор",
        to=User,
        related_name="photos",
        on_delete=models.CASCADE,
    )
