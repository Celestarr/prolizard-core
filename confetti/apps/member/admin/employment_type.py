from django.contrib import admin
from django.utils.translation import gettext_lazy as _

from ..models import EmploymentType


@admin.register(EmploymentType)
class EmploymentTypeAdmin(admin.ModelAdmin):
    pass
