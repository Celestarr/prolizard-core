from django.contrib import admin

from apps.common.admin import ReadOnlyModelAdmin

from .models import (
    AcademicRecord,
    Certification,
    EmploymentType,
    HonorOrAward,
    Language,
    LanguageProficiencyLevel,
    PortfolioTemplate,
    Project,
    Publication,
    ResumeTemplate,
    Skill,
    SkillProficiencyLevel,
    UserPreference,
    WebLink,
    WorkExperience,
)


@admin.register(EmploymentType)
class EmploymentTypeAdmin(ReadOnlyModelAdmin):
    list_display = (
        "id",
        "name",
        "updated_at",
    )
    search_fields = ("name",)
    ordering = ("-id",)


@admin.register(UserPreference)
class UserPreferenceAdmin(admin.ModelAdmin):
    pass


@admin.register(LanguageProficiencyLevel)
class LanguageProficiencyLevelAdmin(ReadOnlyModelAdmin):
    list_display = (
        "id",
        "name",
        "value",
        "updated_at",
    )
    search_fields = ("name",)
    ordering = ("-id",)


@admin.register(SkillProficiencyLevel)
class SkillProficiencyLevelAdmin(ReadOnlyModelAdmin):
    list_display = (
        "id",
        "name",
        "value",
        "updated_at",
    )
    search_fields = ("name",)
    ordering = ("-id",)


@admin.register(AcademicRecord)
class AcademicRecordAdmin(admin.ModelAdmin):
    pass


@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
    pass


@admin.register(WebLink)
class WebLinkAdmin(admin.ModelAdmin):
    pass


@admin.register(WorkExperience)
class WorkExperienceAdmin(admin.ModelAdmin):
    pass


@admin.register(Certification)
class CertificationAdmin(admin.ModelAdmin):
    pass


@admin.register(Language)
class LanguageAdmin(admin.ModelAdmin):
    pass


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    pass


@admin.register(Publication)
class PublicationAdmin(admin.ModelAdmin):
    pass


@admin.register(HonorOrAward)
class HonorOrAwardAdmin(admin.ModelAdmin):
    pass


@admin.register(PortfolioTemplate)
class PortfolioTemplateAdmin(ReadOnlyModelAdmin):
    list_display = (
        "id",
        "name",
        "updated_at",
    )
    search_fields = ("name",)
    ordering = ("-id",)


@admin.register(ResumeTemplate)
class ResumeTemplateAdmin(ReadOnlyModelAdmin):
    list_display = (
        "id",
        "name",
        "slug",
        "updated_at",
    )
    search_fields = (
        "name",
        "slug",
    )
    ordering = ("-id",)
