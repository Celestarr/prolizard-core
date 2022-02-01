from django.db import models
from django.utils.translation import gettext_lazy as _

from confetti.apps.core.models import SmallTimeStampedModel


class LanguageProficiencyLevel(SmallTimeStampedModel):
    name = models.CharField(_("name of language proficiency level"), blank=True, max_length=100, unique=True)
    value = models.PositiveIntegerField(_("mathematical value"), blank=True)

    class Meta:
        verbose_name = _("language proficiency level")
        verbose_name_plural = _("language proficiency levels")
        ordering = ("value",)


class SkillProficiencyLevel(SmallTimeStampedModel):
    name = models.CharField(_("name of skill proficiency level"), blank=True, max_length=100, unique=True)
    value = models.PositiveIntegerField(_("mathematical value"), blank=True)

    class Meta:
        verbose_name = _("skill proficiency level")
        verbose_name_plural = _("skill proficiency levels")
        ordering = ("value",)
