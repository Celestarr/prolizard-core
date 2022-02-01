from django.contrib import admin
from django.utils.translation import gettext
from django.utils.translation import gettext_lazy as _

from confetti.apps.core.models import ConfirmationKey


@admin.register(ConfirmationKey)
class ConfirmationKeyAdmin(admin.ModelAdmin):
    pass
