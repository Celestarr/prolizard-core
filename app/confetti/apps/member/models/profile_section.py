from django.core.exceptions import ValidationError
from django.db import models
from django.utils.translation import gettext_lazy as _

from confetti.apps.core.models import TimeStampedModel

from .employment_type import EmploymentType
from .proficiency_level import LanguageProficiencyLevel, SkillProficiencyLevel


class AcademicRecord(TimeStampedModel):
    degree = models.CharField(_("degree"), blank=True, max_length=150)
    description = models.TextField(_("additional information"), blank=True, default=None, null=True)
    end_date = models.DateField(_("end date"), blank=True, default=None, null=True)
    field_of_study = models.CharField(_("field of study"), blank=True, default=None, max_length=150, null=True)
    grade = models.CharField(_("grade"), blank=True, default=None, max_length=20, null=True)
    is_ongoing = models.BooleanField(_("currently studying"), blank=True, default=False)
    location = models.CharField(_("location of school"), blank=True, default=None, max_length=150, null=True)
    school = models.CharField(_("school"), blank=True, max_length=150)
    start_date = models.DateField(_("start date"), blank=True)
    user = models.ForeignKey("core.User", on_delete=models.CASCADE, related_name="member_academic_record_set")

    def clean(self):
        if self.is_ongoing:
            self.end_date = None

        if not self.end_date and not self.is_ongoing:
            raise ValidationError(
                {
                    "end_date": _("End date is required as you are not studying here currently."),
                }
            )

        if self.end_date < self.start_date:
            raise ValidationError(
                {
                    "end_date": _("End date cannot be before start date."),
                }
            )

    class Meta:
        verbose_name = _("academic record")
        verbose_name_plural = _("academic records")


class Skill(TimeStampedModel):
    name = models.CharField(_("name of skill"), blank=True, max_length=150)
    proficiency = models.ForeignKey(
        SkillProficiencyLevel,
        on_delete=models.CASCADE,
        related_name="proficiency_skill_set",
    )
    user = models.ForeignKey("core.User", on_delete=models.CASCADE, related_name="member_skill_set")

    class Meta:
        verbose_name = _("skill")
        verbose_name_plural = _("skills")


class WebLink(TimeStampedModel):
    href = models.CharField(_("target address"), blank=True, max_length=250)
    label = models.CharField(_("text to display"), blank=True, default=None, max_length=150, null=True)
    user = models.ForeignKey("core.User", on_delete=models.CASCADE, related_name="member_web_link_set")

    class Meta:
        verbose_name = _("web link")
        verbose_name_plural = _("web links")


class WorkExperience(TimeStampedModel):
    company = models.CharField(_("company"), blank=True, max_length=150)
    description = models.TextField(_("additional information"), blank=True, default=None, null=True)
    employment_type = models.ForeignKey(
        EmploymentType,
        on_delete=models.CASCADE,
        related_name="employment_type_work_experience_set",
    )
    end_date = models.DateField(_("end date"), blank=True, default=None, null=True)
    is_ongoing = models.BooleanField(_("currently working"), blank=True, default=False)
    job_title = models.CharField(_("job title"), blank=True, max_length=150)
    location = models.CharField(_("location of company"), blank=True, default=None, max_length=150, null=True)
    start_date = models.DateField(_("start date"), blank=True)
    user = models.ForeignKey("core.User", on_delete=models.CASCADE, related_name="member_work_experience_set")

    def clean(self):
        if self.is_ongoing:
            self.end_date = None

        if not self.end_date and not self.is_ongoing:
            raise ValidationError(
                {
                    "end_date": _("Leaving date is required as you are not working here currently."),
                }
            )

        if self.end_date < self.start_date:
            raise ValidationError(
                {
                    "end_date": _("Leaving date cannot be before joining date."),
                }
            )

    class Meta:
        verbose_name = _("work experience")
        verbose_name_plural = _("work experiences")


class Language(TimeStampedModel):
    name = models.CharField(_("name of language"), blank=True, max_length=100)
    proficiency = models.ForeignKey(
        LanguageProficiencyLevel,
        on_delete=models.CASCADE,
        related_name="proficiency_language_set",
    )
    user = models.ForeignKey("core.User", on_delete=models.CASCADE, related_name="member_language_set")

    class Meta:
        verbose_name = _("language")
        verbose_name_plural = _("languages")


class Project(TimeStampedModel):
    description = models.TextField(_("additional information"), blank=True, default=None, null=True)
    end_date = models.DateField(_("end date"), blank=True, default=None, null=True)
    is_ongoing = models.BooleanField(_("ongoing"), blank=True, default=False)
    name = models.CharField(_("name"), blank=True, max_length=150)
    start_date = models.DateField(_("start date"), blank=True)
    url = models.CharField(_("url"), blank=True, default=None, max_length=150, null=True)
    user = models.ForeignKey("core.User", on_delete=models.CASCADE, related_name="member_project_set")

    def clean(self):
        if self.is_ongoing:
            self.end_date = None

        if not self.end_date and not self.is_ongoing:
            raise ValidationError(
                {
                    "end_date": _("End date is required as you are not working on this project currently."),
                }
            )

        if self.end_date < self.start_date:
            raise ValidationError(
                {
                    "end_date": _("End date cannot be before start date."),
                }
            )

    class Meta:
        verbose_name = _("project")
        verbose_name_plural = _("projects")


class Publication(TimeStampedModel):
    description = models.TextField(_("additional information"), blank=True, default=None, null=True)
    publication_date = models.DateField(_("publication date"), blank=True, default=None, null=True)
    publisher = models.CharField(_("publisher"), blank=True, max_length=150)
    title = models.CharField(_("title"), blank=True, max_length=300)
    url = models.CharField(_("url"), blank=True, default=None, max_length=150, null=True)
    user = models.ForeignKey("core.User", on_delete=models.CASCADE, related_name="member_publication_set")

    class Meta:
        verbose_name = _("publication")
        verbose_name_plural = _("publications")


class HonorOrAward(TimeStampedModel):
    description = models.TextField(_("additional information"), blank=True, default=None, null=True)
    issue_date = models.DateField(_("issue date"), blank=True, default=None, null=True)
    issuer = models.CharField(_("issuer"), blank=True, max_length=150)
    title = models.CharField(_("title"), blank=True, max_length=300)
    user = models.ForeignKey("core.User", on_delete=models.CASCADE, related_name="member_honor_or_award_set")

    class Meta:
        verbose_name = _("user honor or award")
        verbose_name_plural = _("user honors or awards")


class Certification(TimeStampedModel):
    description = models.TextField(_("additional information"), blank=True, default=None, null=True)
    issue_date = models.DateField(_("issue date"), blank=True, default=None, null=True)
    issuer = models.CharField(_("issuer"), blank=True, max_length=150)
    title = models.CharField(_("title"), blank=True, max_length=300)
    user = models.ForeignKey("core.User", on_delete=models.CASCADE, related_name="member_certification_set")

    class Meta:
        verbose_name = _("user certification")
        verbose_name_plural = _("user certifications")
