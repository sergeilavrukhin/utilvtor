from django.contrib import admin
from .models import (
    Companies,
    CompanyWasteCodes,
    CompanyEmails,
    CompanyPhones,
    CompanyRegion,
    CompanySites,
)


class CompanyWasteCodesTabularInline(admin.TabularInline):
    extra = 1
    model = CompanyWasteCodes
    fk_name = "company"
    raw_id_fields = ("waste_code",)


class CompanyCompanyEmailsTabularInline(admin.TabularInline):
    extra = 1
    model = CompanyEmails
    fk_name = "company"


class CompanyCompanyPhonesTabularInline(admin.TabularInline):
    extra = 1
    model = CompanyPhones
    fk_name = "company"


class CompanyCompanyRegionTabularInline(admin.TabularInline):
    extra = 1
    model = CompanyRegion
    fk_name = "company"
    raw_id_fields = ("region",)


class CompanyCompanySitesTabularInline(admin.TabularInline):
    extra = 1
    model = CompanySites
    fk_name = "company"


class CompaniesAdmin(admin.ModelAdmin):
    search_fields = ('itn', 'name')
    inlines = [
        CompanyWasteCodesTabularInline,
        CompanyCompanyEmailsTabularInline,
        CompanyCompanyPhonesTabularInline,
        CompanyCompanySitesTabularInline,
        CompanyCompanyRegionTabularInline,
    ]


admin.site.register(Companies, CompaniesAdmin)
