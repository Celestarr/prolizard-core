from django.contrib import admin

from ..models import LanguageProficiencyLevel, SkillProficiencyLevel


@admin.register(LanguageProficiencyLevel)
class LanguageProficiencyLevelAdmin(admin.ModelAdmin):
    pass


@admin.register(SkillProficiencyLevel)
class SkillProficiencyLevelAdmin(admin.ModelAdmin):
    pass
