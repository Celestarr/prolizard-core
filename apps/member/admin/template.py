from django.contrib import admin

from ..models import PortfolioTemplate, ResumeTemplate


@admin.register(PortfolioTemplate)
class PortfolioTemplateAdmin(admin.ModelAdmin):
    pass


@admin.register(ResumeTemplate)
class ResumeTemplateAdmin(admin.ModelAdmin):
    pass
