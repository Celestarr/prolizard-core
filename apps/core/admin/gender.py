from django.contrib import admin

from ..models import Gender


@admin.register(Gender)
class GenderAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "name",
        "updated_at",
    )
    ordering = ("-id",)

    def has_change_permission(self, request, obj=None):
        return False
