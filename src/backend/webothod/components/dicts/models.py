from django.db import models

activities = [
  "processing",
  "collection",
  "deactivation",
  "transportation",
  "utilization",
  "disposal",
]


class Regions(models.Model):
    class Meta:
        db_table = "regions"
        verbose_name = "Регион"
        verbose_name_plural = "Регионы"
        indexes = [
            models.Index(fields=['code']),
        ]

    text = models.CharField(
        max_length=255,
        verbose_name="Название",
    )
    code = models.PositiveIntegerField(
        default=0,
        verbose_name="Код региона",
    )
    url = models.CharField(
        max_length=255,
    )

    def __str__(self):
        return f"Код региона: {self.code} - {self.text}"


class QueryType(models.Model):
    class Meta:
        db_table = "query_types"
        verbose_name = "Тип заявки"
        verbose_name_plural = "Типы заявок"

    text = models.CharField(
        max_length=40,
        verbose_name="Название",
    )

    def __str__(self):
        return self.text


class Unit(models.Model):
    class Meta:
        db_table = "units"
        verbose_name = "Единица измерения"
        verbose_name_plural = "Единицы измерения"

    text = models.CharField(
        max_length=20,
        verbose_name="Название",
    )

    def __str__(self):
        return self.text


class Aggregation(models.Model):
    class Meta:
        db_table = "aggregations"
        verbose_name = "Агрегатное состояние отхода"
        verbose_name_plural = "Агрегатные состояния отхода"

    code = models.CharField(
        max_length=2,
        default="00",
        verbose_name="Код агрегатного состояния",
    )
    text = models.CharField(
        max_length=255,
        verbose_name="Название",
    )

    def __str__(self):
        return f"Агрегатное состояние: {self.code} - {self.text}"


class WasteCodeCategory(models.Model):
    class Meta:
        db_table = "waste_code_category"
        verbose_name = "Классы отхода"
        verbose_name_plural = "Классы отхода"

    code = models.PositiveIntegerField(
        default=0,
        verbose_name="Класс отхода",
    )
    text = models.CharField(
        max_length=600,
        verbose_name="Название",
    )

    def __str__(self):
        return f"Класс {self.code} - {self.text}"
