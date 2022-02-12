from django.contrib import admin

from ..models import Country


@admin.register(Country)
class CountryAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "name",
        "formal_name",
        "iso_3166_1_alpha_2_code",
        "iso_3166_1_alpha_3_code",
        "iso_3166_1_numeric_code",
        "updated_at",
    )
    search_fields = (
        "name",
        "formal_name",
        "iso_3166_1_alpha_2_code",
        "iso_3166_1_alpha_3_code",
        "iso_3166_1_numeric_code",
    )
    ordering = ("-id",)

    def has_change_permission(self, request, obj=None):
        return False
