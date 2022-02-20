from django.contrib import admin

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
class EmploymentTypeAdmin(admin.ModelAdmin):
    pass


@admin.register(UserPreference)
class UserPreferenceAdmin(admin.ModelAdmin):
    pass


@admin.register(LanguageProficiencyLevel)
class LanguageProficiencyLevelAdmin(admin.ModelAdmin):
    pass


@admin.register(SkillProficiencyLevel)
class SkillProficiencyLevelAdmin(admin.ModelAdmin):
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


@admin.register(PortfolioTemplate)
class PortfolioTemplateAdmin(admin.ModelAdmin):
    pass


@admin.register(ResumeTemplate)
class ResumeTemplateAdmin(admin.ModelAdmin):
    pass
