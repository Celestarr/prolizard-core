from django.db import models
from django.utils.translation import gettext_lazy as _

from .common import SmallTimeStampedModel


class Gender(SmallTimeStampedModel):
    name = models.CharField(blank=True, max_length=50, unique=True)

    class Meta:
        verbose_name = _("gender")
        verbose_name_plural = _("genders")


__all__ = ["Gender"]
