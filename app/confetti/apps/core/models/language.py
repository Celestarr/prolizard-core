from django.core.exceptions import ValidationError
from django.db import models
from django.utils.translation import gettext_lazy as _

from .common import SmallTimeStampedModel


class Language(SmallTimeStampedModel):
    iso_639_1_code = models.CharField(blank=True, max_length=2, unique=True, null=True)
    iso_639_2_code = models.CharField(blank=True, max_length=3, unique=True)
    name = models.CharField(blank=True, max_length=150, unique=True)
    native_name = models.CharField(blank=True, max_length=150, unique=True)

    class Meta:
        verbose_name = _("language")
        verbose_name_plural = _("languages")

    # def clean(self):
    #     cleaned_data = super().clean()

    #     if not cleaned_data.get('alpha_2_code') and not cleaned_data.get('alpha_3_code'):
    #         raise ValidationError({
    #             'alpha_2_code': 'alpha_2_code or alpha_3_code is required',
    #             'alpha_3_code': 'alpha_2_code or alpha_3_code is required',
    #         })


class Locale(SmallTimeStampedModel):
    locale_tag = models.CharField(blank=True, max_length=20, unique=True)
    name = models.CharField(blank=True, max_length=150, unique=True)
    language = models.ForeignKey(Language, blank=True, on_delete=models.CASCADE, related_name="locale_set")
    is_supported = models.BooleanField(blank=True, default=False)

    class Meta:
        verbose_name = _("locale")
        verbose_name_plural = _("locales")


__all__ = ["Language", "Locale"]
