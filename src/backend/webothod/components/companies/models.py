from django.db import models
from ..dicts.models import Regions
from ..waste_codes.models import WasteCodes


class Companies(models.Model):
    name = models.CharField(max_length=255)
    itn = models.CharField(max_length=12)
    latitude = models.CharField(max_length=20, null=True)
    longitude = models.CharField(max_length=20, null=True)
    region = models.ForeignKey(
        Regions,
        on_delete=models.CASCADE,
        related_name="company_region",
        verbose_name="Регион"
    )
    phones = models.CharField(max_length=600)
    emails = models.CharField(max_length=600)
    site = models.CharField(max_length=255)
    activity = models.CharField(max_length=600)
    locality = models.CharField(max_length=600)
    gps = models.CharField(max_length=255)

    class Meta:
        db_table = "companies"
        verbose_name = "Компания"
        verbose_name_plural = "Компании"


class CompanyWasteCodes(models.Model):

    class Meta:
        db_table = "company_waste_codes"
        verbose_name = "Отход с которым работает компания"

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