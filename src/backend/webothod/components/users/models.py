from django.db import models
from django.contrib.auth.models import User


class UserProfile(models.Model):
    user = models.OneToOneField(
        User,
        models.CASCADE,
        related_name='profile',
        verbose_name='Пользователь',
    )
    phone = models.CharField(
        max_length=11,
        verbose_name="Телефон",
    )
    firstname = models.CharField(
        max_length=255,
        verbose_name="Имя",
    )

    class Meta:
        verbose_name = 'Профиль пользователя'
        verbose_name_plural = 'Профили пользователей'
