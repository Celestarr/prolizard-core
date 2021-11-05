from django.contrib import admin
from django.utils.translation import gettext
from django.utils.translation import gettext_lazy as _

from ..models import (
    AcademicRecord,
    Certification,
    HonorOrAward,
    Language,
    Project,
    Publication,
    Skill,
    WebLink,
    WorkExperience,
)


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
