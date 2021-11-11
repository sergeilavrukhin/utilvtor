from django.contrib import admin
from .models import (
    Companies,
    CompanyWasteCodes,
)


class CompaniesAdmin(admin.ModelAdmin):
    pass


class CompanyWasteCodesAdmin(admin.ModelAdmin):
    pass


admin.site.register(Companies, CompaniesAdmin)
admin.site.register(CompanyWasteCodes, CompanyWasteCodesAdmin)
