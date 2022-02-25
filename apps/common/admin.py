from django.contrib import admin

from apps.common.models import Country, Currency, Gender, TimeZone


class ReadOnlyModelAdmin(admin.ModelAdmin):
    def has_change_permission(self, request, obj=None):
        return False

    def has_add_permission(self, request):
        return False

    def has_delete_permission(self, request, obj=None):
        return False


@admin.register(Country)
class CountryAdmin(ReadOnlyModelAdmin):
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


@admin.register(Currency)
class CurrencyAdmin(ReadOnlyModelAdmin):
    list_display = (
        "id",
        "name",
        "symbol",
        "iso_4217_code",
        "iso_4217_numeric_code",
        "updated_at",
    )
    search_fields = (
        "name",
        "iso_4217_code",
        "iso_4217_numeric_code",
    )
    ordering = ("-id",)


@admin.register(Gender)
class GenderAdmin(ReadOnlyModelAdmin):
    list_display = (
        "id",
        "name",
        "updated_at",
    )
    ordering = ("-id",)


@admin.register(TimeZone)
class TimeZoneAdmin(ReadOnlyModelAdmin):
    list_display = (
        "id",
        "name",
        "abbreviation",
        "offset_display_text",
        "updated_at",
    )
    search_fields = ("name", "abbreviation", "offset_display_text")
    ordering = ("offset_minutes",)
