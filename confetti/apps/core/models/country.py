from django.db import models
from django.utils.translation import gettext_lazy as _

from .common import SmallTimeStampedModel


class Country(SmallTimeStampedModel):
    iso_3166_1_alpha_2_code = models.CharField(blank=True, max_length=2, unique=True)
    iso_3166_1_alpha_3_code = models.CharField(blank=True, max_length=3, unique=True)
    iso_3166_1_numeric_code = models.CharField(blank=True, max_length=10, unique=True)
    name = models.CharField(blank=True, max_length=150, unique=True)
    formal_name = models.CharField(blank=True, max_length=150, unique=True)

    class Meta:
        verbose_name = _("country")
        verbose_name_plural = _("countries")


__all__ = ["Country"]
