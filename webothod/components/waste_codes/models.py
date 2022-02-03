from django.db import models
from ..dicts.models import WasteCodeCategory, Aggregation


class WasteCodes(models.Model):
    class Meta:
        db_table = "waste_codes"
        verbose_name = "Код отхода"
        verbose_name_plural = "Коды отхода"
        indexes = [
            models.Index(fields=['code']),
            models.Index(fields=['name']),
            models.Index(fields=['parent_code']),
        ]

    code = models.CharField(
        max_length=11,
        default='',
        verbose_name="Код отхода",
    )
    parent_code = models.CharField(
        max_length=11,
        default='',
        verbose_name="Родительский код отхода",
    )
    name = models.CharField(
        max_length=600,
        verbose_name="Название",
    )
    keywords = models.TextField(
        verbose_name="Ключевые слова",
    )
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

    def __str__(self):
        return f"Код отхода: {self.code} - {self.name}"
