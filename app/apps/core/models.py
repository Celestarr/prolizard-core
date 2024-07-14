from django.core.validators import MinLengthValidator
from django.db import models
from django.utils.translation import gettext_lazy as _

from app.utils.db.models import TimeStampedModelWithSmallId


class Country(TimeStampedModelWithSmallId):
    iso_3166_1_alpha_2_code = models.CharField(blank=True, max_length=2, unique=True)
    iso_3166_1_alpha_3_code = models.CharField(blank=True, max_length=3, unique=True)
    iso_3166_1_numeric_code = models.CharField(blank=True, max_length=10, unique=True)
    name = models.CharField(blank=True, max_length=150, unique=True)
    formal_name = models.CharField(blank=True, max_length=150, unique=True)

    class Meta:
        verbose_name = _("country")
        verbose_name_plural = _("countries")
        ordering = ("id",)


class Currency(TimeStampedModelWithSmallId):
    iso_4217_code = models.CharField(blank=True, max_length=3, unique=True)
    iso_4217_numeric_code = models.CharField(blank=True, max_length=10, unique=True)
    name = models.CharField(blank=True, max_length=100, unique=True)
    symbol = models.CharField(blank=True, max_length=20)

    class Meta:
        verbose_name = _("currency")
        verbose_name_plural = _("currencies")
        ordering = ("id",)


class SupportedLocale(TimeStampedModelWithSmallId):
    locale_tag = models.CharField(blank=True, max_length=20, unique=True)
    iso_639_1_code = models.CharField(blank=True, max_length=2)
    iso_639_2_code = models.CharField(blank=True, max_length=3)
    name = models.CharField(blank=True, max_length=150, unique=True)
    native_name = models.CharField(blank=True, max_length=150, unique=True)

    class Meta:
        verbose_name = _("supported locale")
        verbose_name_plural = _("supported locales")
        ordering = ("id",)


class TimeZone(TimeStampedModelWithSmallId):
    abbreviation = models.CharField(blank=True, db_index=True, max_length=20)
    name = models.CharField(blank=True, max_length=150, unique=True)
    offset_display_text = models.CharField(blank=True, max_length=20)
    offset_text = models.CharField(blank=True, max_length=20)
    offset_text_clean = models.CharField(blank=True, db_index=True, max_length=20)
    offset_minutes = models.SmallIntegerField(blank=True)

    class Meta:
        verbose_name = _("time zone")
        verbose_name_plural = _("time zones")
        ordering = ("offset_minutes",)
