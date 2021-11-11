from django.db import models
from ..dicts.models import Regions
from ..waste_codes.models import WasteCodes


class Companies(models.Model):
    name = models.CharField(max_length=255, verbose_name="Название компании")
    itn = models.CharField(max_length=12, verbose_name="ИНН")
    latitude = models.CharField(max_length=20, null=True, verbose_name="Широта")
    longitude = models.CharField(max_length=20, null=True, verbose_name="Долгота")
    region = models.ForeignKey(
        Regions,
        on_delete=models.CASCADE,
        related_name="company_region",
        verbose_name="Регион"
    )
    phones = models.CharField(max_length=600, verbose_name="Телефон")
    emails = models.CharField(max_length=600, verbose_name="Email")
    site = models.CharField(max_length=255, verbose_name="Сайт")
    activity = models.CharField(max_length=600, verbose_name="Типы отходов с которыми работает")
    locality = models.CharField(max_length=600, verbose_name="Расположение?")
    gps = models.CharField(max_length=255, verbose_name="Координаты")

    class Meta:
        db_table = "companies"
        verbose_name = "Компания"
        verbose_name_plural = "Компании"


class CompanyWasteCodes(models.Model):

    class Meta:
        db_table = "company_waste_codes"
        verbose_name = "Отход с которым работает компания"
        verbose_name_plural = "Отходы с которым работают компании"

    company = models.ForeignKey(
        Companies,
        on_delete=models.CASCADE,
        related_name="company",
        verbose_name="Компания"
    )

    waste_code = models.ForeignKey(
        WasteCodes,
        on_delete=models.CASCADE,
        related_name="waste_code",
        verbose_name="Код отхода"
    )