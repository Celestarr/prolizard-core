from django.contrib import admin
from django.utils.translation import gettext
from django.utils.translation import gettext_lazy as _

from ..models import PortfolioTemplate, ResumeTemplate


@admin.register(PortfolioTemplate)
class PortfolioTemplateAdmin(admin.ModelAdmin):
    pass


@admin.register(ResumeTemplate)
class ResumeTemplateAdmin(admin.ModelAdmin):
    pass
