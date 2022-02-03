from django.db import models
from django.contrib.auth.models import User
from ..dicts.models import Regions, QueryType


class Queries(models.Model):
    class Meta:
        db_table = "queries"
        verbose_name = "Заявка"
        verbose_name_plural = "Заявка"

    created_at = models.DateTimeField(
        "Дата и время создания",
        auto_now_add=True,
    )
    waste = models.CharField(
        max_length=255,
        verbose_name="Название отхода",
    )
    region = models.ForeignKey(
        Regions,
        on_delete=models.CASCADE,
        related_name="query_region",
        verbose_name="Регион"
    )
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="user",
        verbose_name="Автор"
    )
    type = models.ForeignKey(
        QueryType,
        on_delete=models.CASCADE,
        related_name="type",
        verbose_name="Тип заявки"
    )
    description = models.TextField(
        verbose_name="Описание заявки",
    )
