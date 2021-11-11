from django.contrib import admin
from .models import (
    Regions,
    QueryType,
    Unit,
    Aggregation,
    WasteCodeCategory,
)


class RegionsAdmin(admin.ModelAdmin):
    pass


class QueryTypeAdmin(admin.ModelAdmin):
    pass


class UnitAdmin(admin.ModelAdmin):
    pass


class AggregationAdmin(admin.ModelAdmin):
    pass


class WasteCodeCategoryAdmin(admin.ModelAdmin):
    pass


admin.site.register(Regions, RegionsAdmin)
admin.site.register(QueryType, QueryTypeAdmin)
admin.site.register(Unit, UnitAdmin)
admin.site.register(Aggregation, AggregationAdmin)
admin.site.register(WasteCodeCategory, WasteCodeCategoryAdmin)
