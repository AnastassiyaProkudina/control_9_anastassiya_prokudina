from django.contrib.auth.models import AbstractUser
from django.db import models


class Account(AbstractUser):
    email = models.EmailField(
        verbose_name="Электронная почта", unique=True, blank=True
    )

    avatar = models.ImageField(
        null=True,
        blank=True,
        upload_to="user_pic",
        verbose_name="Аватар",
        default="user_pic/default_user_pic.jpeg",
    )
    bio = models.TextField(verbose_name="Информация о пользователе", blank=True)

    class Meta:
        verbose_name = "Профиль"
        verbose_name_plural = "Профили"

    def __str__(self):
        return self.username
