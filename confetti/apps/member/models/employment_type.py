from django.db import models
from django.utils.translation import gettext_lazy as _

from confetti.apps.core.models import SmallTimeStampedModel


class EmploymentType(SmallTimeStampedModel):
    name = models.CharField(_("name of employment type"), blank=True, max_length=100, unique=True)

    class Meta:
        verbose_name = _("employment type")
        verbose_name_plural = _("employment types")
