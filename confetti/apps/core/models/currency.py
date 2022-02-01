from django.db import models
from django.utils.translation import gettext_lazy as _

from .common import SmallTimeStampedModel


class Currency(SmallTimeStampedModel):
    iso_4217_code = models.CharField(blank=True, max_length=3, unique=True)
    iso_4217_numeric_code = models.CharField(blank=True, max_length=10, unique=True)
    name = models.CharField(blank=True, max_length=100, unique=True)
    symbol = models.CharField(blank=True, max_length=20)
    major_unit = models.CharField(blank=True, max_length=50)
    minor_unit = models.CharField(blank=True, max_length=50)
    decimal_places = models.PositiveSmallIntegerField(blank=True, default=2)

    class Meta:
        verbose_name = _("currency")
        verbose_name_plural = _("currencies")


__all__ = ["Currency"]
