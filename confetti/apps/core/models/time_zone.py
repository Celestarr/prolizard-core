from django.db import models
from django.utils.translation import gettext_lazy as _

from .common import SmallTimeStampedModel


class TimeZone(SmallTimeStampedModel):
    abbreviation = models.CharField(blank=True, db_index=True, max_length=20)
    name = models.CharField(blank=True, max_length=150, unique=True)
    offset_display_text = models.CharField(blank=True, max_length=20)
    offset_text = models.CharField(blank=True, max_length=20)
    offset_text_clean = models.CharField(blank=True, db_index=True, max_length=20)
    offset_minutes = models.SmallIntegerField(blank=True)

    class Meta:
        verbose_name = _("time_zone")
        verbose_name_plural = _("time_zones")
        ordering = ("offset_minutes",)


__all__ = ["TimeZone"]
