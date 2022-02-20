from django.contrib import admin

from apps.common.models import Country, Currency, Gender, TimeZone


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


@admin.register(Currency)
class CurrencyAdmin(admin.ModelAdmin):
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

    def has_change_permission(self, request, obj=None):
        return False


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
