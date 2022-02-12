from django.contrib import admin

from apps.core.models import ConfirmationKey


@admin.register(ConfirmationKey)
class ConfirmationKeyAdmin(admin.ModelAdmin):
    pass
