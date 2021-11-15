from django.db import models


class Regions(models.Model):
    text = models.CharField(max_length=255, verbose_name="Название")
    code = models.PositiveIntegerField(default=0, verbose_name="Код региона")
    url = models.CharField(max_length=255)

    class Meta:
        db_table = "regions"
        verbose_name = "Регион"
        verbose_name_plural = "Регионы"

    def __str__(self):
        return f"Код региона: {self.code} - {self.text}"


class QueryType(models.Model):
    text = models.CharField(max_length=40, verbose_name="Название")

    class Meta:
        db_table = "query_types"
        verbose_name = "Тип заявки"
        verbose_name_plural = "Типы заявок"

    def __str__(self):
        return self.text


class Unit(models.Model):
    text = models.CharField(max_length=20, verbose_name="Название")

    class Meta:
        db_table = "units"
        verbose_name = "Единица измерения"
        verbose_name_plural = "Единицы измерения"

    def __str__(self):
        return self.text


class Aggregation(models.Model):
    text = models.CharField(max_length=255, verbose_name="Название")

    class Meta:
        db_table = "aggregations"
        verbose_name = "Агрегатное состояние отхода"
        verbose_name_plural = "Агрегатные состояния отхода"

    def __str__(self):
        return self.text


class WasteCodeCategory(models.Model):
    code = models.PositiveIntegerField(default=0, verbose_name="Класс отхода")
    text = models.CharField(max_length=600, verbose_name="Название")

    class Meta:
        db_table = "waste_code_category"
        verbose_name = "Классы отхода"
        verbose_name_plural = "Классы отхода"

    def __str__(self):
        return f"Класс {self.code} - {self.text}"
