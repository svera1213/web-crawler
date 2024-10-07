from django.contrib import admin

from . import models


@admin.register(models.Headline)
class HeadlineAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "news_id",
        "title",
        "comments",
        "points",
    )
    search_fields = ("id", "news_id", "title")
