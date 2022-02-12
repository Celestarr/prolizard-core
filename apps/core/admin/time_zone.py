from django.contrib import admin

from ..models import TimeZone


@admin.register(TimeZone)
class TimeZoneAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "name",
        "abbreviation",
        "offset_display_text",
        "updated_at",
    )
    search_fields = ("name", "abbreviation", "offset_display_text")
    ordering = ("offset_minutes",)

    def has_change_permission(self, request, obj=None):
        return False
