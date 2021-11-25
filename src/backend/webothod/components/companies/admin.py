from django.contrib import admin
from .models import (
    Companies,
    CompanyWasteCodes,
)


class CompanyWasteCodesTabularInline(admin.TabularInline):
    model = CompanyWasteCodes
    fk_name = "company"
    raw_id_fields = ("waste_code",)


class CompaniesAdmin(admin.ModelAdmin):
    search_fields = ('itn', 'name')
    inlines = [CompanyWasteCodesTabularInline]


admin.site.register(Companies, CompaniesAdmin)
