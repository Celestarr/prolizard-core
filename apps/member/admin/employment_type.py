from django.contrib import admin

from ..models import EmploymentType


@admin.register(EmploymentType)
class EmploymentTypeAdmin(admin.ModelAdmin):
    pass
