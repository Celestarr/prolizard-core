from django.db import models
from django.utils.translation import gettext_lazy as _

from confetti.apps.core.models import TimeStampedModel


class PortfolioTemplate(TimeStampedModel):
    name = models.CharField(_("name of template"), blank=True, max_length=100, unique=True)

    class Meta:
        verbose_name = _("portfolio template")
        verbose_name_plural = _("portfolio templates")


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
