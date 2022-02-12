from django.apps import apps
from django.db import models
from django.utils.translation import gettext_lazy as _

from apps.core.models import TimeStampedModel
from apps.member.constants import UI_MODE_DARK, UI_MODE_LIGHT, UI_MODE_SYSTEM


def get_default_resume_template():
    ResumeTemplate = apps.get_model("member", "ResumeTemplate")
    template = ResumeTemplate.objects.all().first()

    return template.id if template else None


class MemberPreference(TimeStampedModel):
    user = models.OneToOneField("core.User", on_delete=models.CASCADE, related_name="member_preference")
    UI_MODE_CHOICES = (
        (UI_MODE_DARK, UI_MODE_DARK),
        (UI_MODE_LIGHT, UI_MODE_LIGHT),
        (UI_MODE_SYSTEM, UI_MODE_SYSTEM),
    )
    ui_mode = models.CharField(blank=True, choices=UI_MODE_CHOICES, max_length=20, default=UI_MODE_SYSTEM)
    portfolio_template = models.ForeignKey(
        "PortfolioTemplate",
        null=True,
        on_delete=models.SET_NULL,
        related_name="member_preference_set",
    )
    resume_template = models.ForeignKey(
        "ResumeTemplate",
        on_delete=models.PROTECT,
        related_name="member_preference_set",
        default=get_default_resume_template,
    )

    class Meta:
        verbose_name = _("member preference")
        verbose_name_plural = _("member preference")
