from django.apps import apps
from django.db import models
from django.utils.translation import gettext_lazy as _

from confetti.apps.core.models import TimeStampedModel


def get_default_resume_template():
    ResumeTemplate = apps.get_model("member", "ResumeTemplate")
    template = ResumeTemplate.objects.all().first()

    return template.id if template else None


class MemberPreference(TimeStampedModel):
    user = models.OneToOneField("core.User", on_delete=models.CASCADE, related_name="member_preference")
    web_app_dark_mode = models.BooleanField(blank=True, default=False)
    portfolio_template = models.ForeignKey(
        "PortfolioTemplate", null=True, on_delete=models.SET_NULL, related_name="member_preference_set"
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
