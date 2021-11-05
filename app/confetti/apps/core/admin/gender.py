from django.contrib import admin
from django.utils.translation import gettext
from django.utils.translation import gettext_lazy as _

from ..models import Gender


@admin.register(Gender)
class GenderAdmin(admin.ModelAdmin):
    pass
