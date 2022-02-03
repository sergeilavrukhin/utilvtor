from django.contrib import admin
from .models import (
    Queries,
)


class QueriesAdmin(admin.ModelAdmin):
    pass


admin.site.register(Queries, QueriesAdmin)
