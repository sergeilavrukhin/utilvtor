from django.db import models
from django.utils.timezone import now
from ..dicts.models import Regions
from ..waste_codes.models import WasteCodes


class Companies(models.Model):
    class Meta:
        db_table = "companies"
        verbose_name = "Компания"
        verbose_name_plural = "Компании"
        indexes = [
            models.Index(fields=['itn']),
            models.Index(fields=['name']),
            models.Index(fields=['region']),
        ]
    name = models.CharField(
        max_length=255,
        verbose_name="Название компании",
    )
    itn = models.CharField(
        max_length=12,
        verbose_name="ИНН",
    )
    latitude = models.CharField(
        max_length=20,
        null=True,
        blank=True,
        verbose_name="Широта",
    )
    longitude = models.CharField(
        max_length=20,
        null=True,
        blank=True,
        verbose_name="Долгота",
    )
    region = models.ForeignKey(
        Regions,
        on_delete=models.CASCADE,
        related_name="company_region",
        null=True,
        verbose_name="Регион",
    )
    phones = models.CharField(
        max_length=600,
        null=True,
        blank=True,
        verbose_name="Телефон",
    )
    emails = models.CharField(
        max_length=600,
        null=True,
        blank=True,
        verbose_name="Email",
    )
    site = models.CharField(
        max_length=255,
        null=True,
        blank=True,
        verbose_name="Сайт",
    )
    activity = models.CharField(
        max_length=600,
        null=True,
        blank=True,
        verbose_name="Типы отходов с которыми работает",
    )
    locality = models.CharField(
        max_length=600,
        verbose_name="Адрес",
    )
    gps = models.CharField(
        max_length=255,
        null=True,
        blank=True,
        verbose_name="Координаты",
    )
    actual = models.BooleanField(
        default=False,
        verbose_name="Актуальные данные",
    )
    actual_at = models.DateTimeField(
        default=now,
        editable=True,
        verbose_name="Дата и время проверки актуальности",
    )
    description = models.TextField(
        default="",
        null=True,
        blank=True,
        verbose_name="Описание компании",
    )

    def __str__(self):
        return f"Компания {self.itn} - {self.name}"


class CompanyWasteCodes(models.Model):
    class Meta:
        db_table = "company_waste_codes"
        verbose_name = "Отход с которым работает компания"
        verbose_name_plural = "Отходы с которым работают компании"
        indexes = [
            models.Index(fields=['company']),
            models.Index(fields=['waste_code']),
            models.Index(fields=['activity']),
        ]

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
    activity = models.CharField(
        max_length=600,
        default='',
        verbose_name="Типы отходов с которыми работает",
    )


class CompanyPhones(models.Model):
    class Meta:
        db_table = "company_phones"
        verbose_name = "Телефон компании"
        verbose_name_plural = "Телефоны компании"
        indexes = [
            models.Index(fields=['company']),
        ]

    company = models.ForeignKey(
        Companies,
        on_delete=models.CASCADE,
        related_name="company_phones",
        verbose_name="Компания"
    )
    phone = models.CharField(
        max_length=255,
        null=True,
        blank=True,
        verbose_name="Телефон",
    )

    def __str__(self):
        return self.phone


class CompanySites(models.Model):
    class Meta:
        db_table = "company_sites"
        verbose_name = "Сайт компании"
        verbose_name_plural = "Сайты компании"
        indexes = [
            models.Index(fields=['company']),
        ]

    company = models.ForeignKey(
        Companies,
        on_delete=models.CASCADE,
        related_name="company_sites",
        verbose_name="Компания"
    )
    site = models.CharField(
        max_length=255,
        null=True,
        blank=True,
        verbose_name="Сайт",
    )

    def __str__(self):
        return self.site


class CompanyEmails(models.Model):
    class Meta:
        db_table = "company_emails"
        verbose_name = "Email компании"
        verbose_name_plural = "Emails компании"
        indexes = [
            models.Index(fields=['company']),
        ]

    company = models.ForeignKey(
        Companies,
        on_delete=models.CASCADE,
        related_name="company_emails",
        verbose_name="Компания"
    )
    email = models.CharField(
        max_length=255,
        null=True,
        blank=True,
        verbose_name="Email",
    )

    def __str__(self):
        return self.email


class CompanyRegion(models.Model):
    class Meta:
        db_table = "company_regions"
        verbose_name = "Регион компании"
        verbose_name_plural = "Регионы компании"
        indexes = [
            models.Index(fields=['company']),
        ]

    company = models.ForeignKey(
        Companies,
        on_delete=models.CASCADE,
        related_name="company_region_company",
        verbose_name="Компания"
    )
    region = models.ForeignKey(
        Regions,
        on_delete=models.CASCADE,
        related_name="company_region_region",
        null=True,
        verbose_name="Регион",
    )

    def __str__(self):
        return self.region.text
