from django.db import models
from ..dicts.models import WasteCodeCategory, Aggregation


class WasteCodes(models.Model):
    parent = models.ForeignKey(
        "self",
        on_delete=models.CASCADE,
        related_name="parent_waste_code",
        verbose_name="Родительский код отхода",
        null=True,
    )
    name = models.CharField(max_length=600)
    keywords = models.TextField()
    category = models.ForeignKey(
        WasteCodeCategory,
        on_delete=models.CASCADE,
        related_name="waste_code_category",
        verbose_name="Категория отходоа",
        null=True,
    )
    aggregation = models.ForeignKey(
        Aggregation,
        on_delete=models.CASCADE,
        related_name="aggregation",
        verbose_name="Агрегатное состояние отходоа",
        null=True,
    )

    url = models.CharField(max_length=255)
    iso = models.CharField(max_length=10)
    activity = models.CharField(max_length=600)

    class Meta:
        db_table = "waste_codes"
        verbose_name = "Код отхода"
        verbose_name_plural = "Коды отхода"
