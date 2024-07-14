from django.contrib import admin

from app.apps.core.admin import ReadOnlyModelAdmin

from .models import (
    AcademicRecord,
    Certification,
    HonorOrAward,
    Language,
    Project,
    Publication,
    ResumeTemplate,
    Skill,
    UserPreference,
    WebLink,
    WorkExperience,
)


@admin.register(UserPreference)
class UserPreferenceAdmin(admin.ModelAdmin):
    pass


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
