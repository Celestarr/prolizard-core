from django.db import models
from django.utils.translation import gettext_lazy as _

from confetti.apps.core.models import TimeStampedModel


class PortfolioTemplate(TimeStampedModel):
    name = models.CharField(_("name of template"), blank=True, max_length=100, unique=True)

    class Meta:
        verbose_name = _("portfolio template")
        verbose_name_plural = _("portfolio templates")


class ResumeTemplate(TimeStampedModel):
    name = models.CharField(_("name of template"), blank=True, max_length=100, unique=True)
    template_file_name = models.CharField(
        _("name of file containing template definition"),
        blank=True,
        max_length=150,
        unique=True,
    )
    puppeteer_config = models.JSONField(blank=True, default=dict)

    class Meta:
        verbose_name = _("resume template")
        verbose_name_plural = _("resume templates")
