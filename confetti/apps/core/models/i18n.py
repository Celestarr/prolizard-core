from django.core.exceptions import ValidationError
from django.db import models
from django.utils.translation import gettext_lazy as _

from .common import SmallTimeStampedModel


class SupportedLocale(SmallTimeStampedModel):
    locale_tag = models.CharField(blank=True, max_length=20, unique=True)
    iso_639_1_code = models.CharField(blank=True, max_length=2)
    iso_639_2_code = models.CharField(blank=True, max_length=3)
    name = models.CharField(blank=True, max_length=150, unique=True)
    native_name = models.CharField(blank=True, max_length=150, unique=True)

    class Meta:
        verbose_name = _("supported locale")
        verbose_name_plural = _("supported locales")


__all__ = ["SupportedLocale"]
