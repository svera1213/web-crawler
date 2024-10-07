from django.contrib import admin

from . import models


@admin.register(models.UsageTracker)
class UsageTrackerAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "timestamp",
        "host",
        "ordering_type",
    )
    search_fields = ("host", "ordering_type", "id")
