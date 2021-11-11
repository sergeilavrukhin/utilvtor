from django.db import models


class Regions(models.Model):
    text = models.CharField(max_length=255, verbose_name="Название")
    url = models.CharField(max_length=255)
    iso = models.CharField(max_length=10, verbose_name="Код региона")
    activity = models.CharField(max_length=600, verbose_name="С какими кодами работают в регионе")

    class Meta:
        db_table = "regions"
        verbose_name = "Регион"
        verbose_name_plural = "Регионы"


class QueryType(models.Model):
    class Meta:
        db_table = "query_types"
        verbose_name = "Тип заявки"
        verbose_name_plural = "Типы заявок"
    text = models.CharField(max_length=40, verbose_name="Название")


class Unit(models.Model):
    class Meta:
        db_table = "units"
        verbose_name = "Единица измерения"
        verbose_name_plural = "Единицы измерения"
    text = models.CharField(max_length=20, verbose_name="Название")


class Aggregation(models.Model):
    class Meta:
        db_table = "aggregations"
        verbose_name = "Агрегатное состояние"
        verbose_name_plural = "Агрегатные состояния"
    text = models.CharField(max_length=255, verbose_name="Название")


class WasteCodeCategory(models.Model):
    class Meta:
        db_table = "waste_code_category"
        verbose_name = "Категория отхода"
        verbose_name_plural = "Категории отхода"
    text = models.CharField(max_length=600, verbose_name="Название")
