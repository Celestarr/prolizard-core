from django.apps import apps
from django.core.exceptions import ValidationError
from django.db import models
from django.utils.translation import gettext_lazy as _

from app.utils.db.models import TimeStampedModel, TimeStampedModelWithSmallId


class ResumeTemplate(TimeStampedModel):
    slug = models.CharField(_("slug/unique id of template"), blank=True, max_length=100, unique=True)
    name = models.CharField(_("name of template"), blank=True, max_length=100)
    template_entrypoint = models.CharField(
        _("name of entrypoint file containing latex template definition"),
        blank=True,
        max_length=150,
    )

    class Meta:
        verbose_name = _("resume template")
        verbose_name_plural = _("resume templates")


def get_default_resume_template():
    _ResumeTemplate = apps.get_model("profile", "ResumeTemplate")  # pylint: disable=invalid-name
    template = _ResumeTemplate.objects.all().first()

    return template.id if template else None


class UserPreference(TimeStampedModel):
    resume_template = models.ForeignKey(
        "ResumeTemplate",
        on_delete=models.PROTECT,
        related_name="user_preference_set",
        default=get_default_resume_template,
    )

    UI_MODE_CHOICES = (
        ("DARK", "Dark"),
        ("LIGHT", "Light"),
        ("SYSTEM", "System"),
    )
    ui_mode = models.CharField(blank=True, choices=UI_MODE_CHOICES, default=UI_MODE_CHOICES[-1][0], max_length=20)

    user = models.OneToOneField("user_management.User", on_delete=models.CASCADE, related_name="preference")

    user_editable_fields = [
        "resume_template",
        "ui_mode",
    ]

    class Meta:
        verbose_name = _("preference")
        verbose_name_plural = _("preferences")


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
    user = models.ForeignKey("user_management.User", on_delete=models.CASCADE, related_name="academic_record_set")

    user_editable_fields = [
        "degree",
        "description",
        "end_date",
        "field_of_study",
        "grade",
        "is_ongoing",
        "location",
        "school",
        "start_date",
    ]

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

    def get_form_layout_config(self):
        return [
            {"row": 1, "fields": ["school", "location"], "sizes": [6, 6]},
            {"row": 2, "fields": ["degree", "field_of_study"], "sizes": [6, 6]},
            {"row": 3, "fields": ["start_date", "end_date"], "sizes": [6, 6]},
            {"row": 4, "fields": ["grade"], "sizes": [12]},
            {"row": 5, "fields": ["description"], "sizes": [12]},
        ]


class Skill(TimeStampedModel):
    name = models.CharField(_("name of skill"), blank=True, max_length=150)

    # NOTE: Order matters.
    PROFICIENCY_LEVEL_CHOICES = [
        ("novice", "Novice"),
        ("advanced_beginner", "Advanced Beginner"),
        ("competent", "Competent"),
        ("proficient", "Proficient"),
        ("expert", "Expert"),
    ]
    proficiency = models.CharField(
        blank=True,
        choices=PROFICIENCY_LEVEL_CHOICES,
        max_length=50,
    )

    user = models.ForeignKey("user_management.User", on_delete=models.CASCADE, related_name="skill_set")

    user_editable_fields = [
        "name",
        "proficiency",
    ]

    class Meta:
        verbose_name = _("skill")
        verbose_name_plural = _("skills")

    def get_form_layout_config(self):
        return [
            {"row": 1, "fields": ["name"], "sizes": [12]},
            {"row": 2, "fields": ["proficiency"], "sizes": [12]},
        ]


class WebLink(TimeStampedModel):
    href = models.CharField(_("target address"), blank=True, max_length=250)
    label = models.CharField(_("text to display"), blank=True, default=None, max_length=150, null=True)
    user = models.ForeignKey("user_management.User", on_delete=models.CASCADE, related_name="web_link_set")

    user_editable_fields = ["href", "label"]

    class Meta:
        verbose_name = _("web link")
        verbose_name_plural = _("web links")

    def get_form_layout_config(self):
        return [
            {"row": 1, "fields": ["label"], "sizes": [12]},
            {"row": 2, "fields": ["href"], "sizes": [12]},
        ]


class WorkExperience(TimeStampedModel):
    company = models.CharField(_("company"), blank=True, max_length=150)
    description = models.TextField(_("additional information"), blank=True, default=None, null=True)

    EMPLOYMENT_TYPE_CHOICES = [
        ("CASUAL", "Casual"),
        ("FULL_TIME", "Full-time"),
        ("CONTRACT", "Contract/Fixed term"),
        ("PART_TIME", "Part-time"),
        ("TRAINEE", "Trainee/Apprentice"),
    ]
    employment_type = models.CharField(
        blank=True,
        choices=EMPLOYMENT_TYPE_CHOICES,
        max_length=50,
    )

    end_date = models.DateField(_("end date"), blank=True, default=None, null=True)
    is_ongoing = models.BooleanField(_("currently working"), blank=True, default=False)
    job_title = models.CharField(_("job title"), blank=True, max_length=150)
    location = models.CharField(_("location of company"), blank=True, default=None, max_length=150, null=True)
    start_date = models.DateField(_("start date"), blank=True)
    user = models.ForeignKey("user_management.User", on_delete=models.CASCADE, related_name="work_experience_set")

    user_editable_fields = [
        "company",
        "description",
        "employment_type",
        "end_date",
        "is_ongoing",
        "job_title",
        "location",
        "start_date",
    ]

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

    def get_form_layout_config(self):
        return [
            {"row": 1, "fields": ["company", "location"], "sizes": [6, 6]},
            {"row": 2, "fields": ["job_title", "employment_type"], "sizes": [6, 6]},
            {"row": 3, "fields": ["start_date", "end_date"], "sizes": [6, 6]},
            {"row": 4, "fields": ["description"], "sizes": [12]},
        ]


class Language(TimeStampedModel):
    name = models.CharField(_("name of language"), blank=True, max_length=100)

    # NOTE: Order matters.
    PROFICIENCY_LEVEL_CHOICES = [
        ("ELEMENTARY", "Elementary Proficiency"),
        ("LIMITED_WORKING", "Limited Working Proficiency"),
        ("PROFESSIONAL", "Professional Working Proficiency"),
        ("FULL_PROFESSIONAL", "Full Professional Proficiency"),
        ("NATIVE", "Native/Bilingual Proficiency"),
    ]
    proficiency = models.CharField(
        blank=True,
        choices=PROFICIENCY_LEVEL_CHOICES,
        max_length=50,
    )
    user = models.ForeignKey("user_management.User", on_delete=models.CASCADE, related_name="language_set")

    user_editable_fields = [
        "name",
        "proficiency",
    ]

    class Meta:
        verbose_name = _("language")
        verbose_name_plural = _("languages")

    def get_form_layout_config(self):
        return [
            {"row": 1, "fields": ["name"], "sizes": [12]},
            {"row": 2, "fields": ["proficiency"], "sizes": [12]},
        ]


class Project(TimeStampedModel):
    description = models.TextField(_("additional information"), blank=True, default=None, null=True)
    end_date = models.DateField(_("end date"), blank=True, default=None, null=True)
    is_ongoing = models.BooleanField(_("ongoing"), blank=True, default=False)
    name = models.CharField(_("name"), blank=True, max_length=150)
    start_date = models.DateField(_("start date"), blank=True)
    url = models.CharField(_("url"), blank=True, default=None, max_length=150, null=True)
    user = models.ForeignKey("user_management.User", on_delete=models.CASCADE, related_name="project_set")

    user_editable_fields = [
        "description",
        "end_date",
        "is_ongoing",
        "name",
        "start_date",
        "url",
    ]

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

    def get_form_layout_config(self):
        return [
            {"row": 1, "fields": ["name"], "sizes": [12]},
            {"row": 2, "fields": ["url"], "sizes": [12]},
            {"row": 3, "fields": ["start_date", "end_date"], "sizes": [6, 6]},
            {"row": 4, "fields": ["description"], "sizes": [12]},
        ]


class Publication(TimeStampedModel):
    description = models.TextField(_("additional information"), blank=True, default=None, null=True)
    publication_date = models.DateField(_("publication date"), blank=True, default=None, null=True)
    publisher = models.CharField(_("publisher"), blank=True, max_length=150)
    title = models.CharField(_("title"), blank=True, max_length=300)
    url = models.CharField(_("url"), blank=True, default=None, max_length=150, null=True)
    user = models.ForeignKey("user_management.User", on_delete=models.CASCADE, related_name="publication_set")

    user_editable_fields = [
        "description",
        "publication_date",
        "publisher",
        "title",
        "url",
    ]

    class Meta:
        verbose_name = _("publication")
        verbose_name_plural = _("publications")

    def get_form_layout_config(self):
        return [
            {"row": 1, "fields": ["title"], "sizes": [12]},
            {"row": 2, "fields": ["url"], "sizes": [12]},
            {"row": 3, "fields": ["publisher", "publication_date"], "sizes": [6, 6]},
            {"row": 4, "fields": ["description"], "sizes": [12]},
        ]


class HonorOrAward(TimeStampedModel):
    description = models.TextField(_("additional information"), blank=True, default=None, null=True)
    issue_date = models.DateField(_("issue date"), blank=True, default=None, null=True)
    issuer = models.CharField(_("issuer"), blank=True, max_length=150)
    title = models.CharField(_("title"), blank=True, max_length=300)
    user = models.ForeignKey("user_management.User", on_delete=models.CASCADE, related_name="honor_or_award_set")

    user_editable_fields = [
        "description",
        "issue_date",
        "issuer",
        "title",
    ]

    class Meta:
        verbose_name = _("user honor or award")
        verbose_name_plural = _("user honors or awards")

    def get_form_layout_config(self):
        return [
            {"row": 1, "fields": ["title"], "sizes": [12]},
            {"row": 2, "fields": ["issuer", "issue_date"], "sizes": [6, 6]},
            {"row": 3, "fields": ["description"], "sizes": [12]},
        ]


class Certification(TimeStampedModel):
    description = models.TextField(_("additional information"), blank=True, default=None, null=True)
    issue_date = models.DateField(_("issue date"), blank=True, default=None, null=True)
    issuer = models.CharField(_("issuer"), blank=True, max_length=150)
    title = models.CharField(_("title"), blank=True, max_length=300)
    user = models.ForeignKey("user_management.User", on_delete=models.CASCADE, related_name="certification_set")

    user_editable_fields = [
        "description",
        "issue_date",
        "issuer",
        "title",
    ]

    class Meta:
        verbose_name = _("user certification")
        verbose_name_plural = _("user certifications")

    def get_form_layout_config(self):
        return [
            {"row": 1, "fields": ["title"], "sizes": [12]},
            {"row": 2, "fields": ["issuer", "issue_date"], "sizes": [6, 6]},
            {"row": 3, "fields": ["description"], "sizes": [12]},
        ]
