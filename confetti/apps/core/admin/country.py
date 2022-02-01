from django.contrib import admin
from django.utils.translation import gettext
from django.utils.translation import gettext_lazy as _

from ..models import Country


@admin.register(Country)
class CountryAdmin(admin.ModelAdmin):
    pass
