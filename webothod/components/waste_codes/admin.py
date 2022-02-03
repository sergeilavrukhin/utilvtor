from django.contrib import admin
from .models import (
    WasteCodes,
)


class WasteCodesAdmin(admin.ModelAdmin):
    pass


admin.site.register(WasteCodes, WasteCodesAdmin)
