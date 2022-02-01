from django.conf import settings
from django.core.validators import MinLengthValidator
from django.db import models
from django.utils.translation import gettext_lazy as _

from .common import TimeStampedModel


class ConfirmationKey(TimeStampedModel):
    key = models.CharField(
        _("key"),
        blank=True,
        max_length=settings.FIELD_META["confirmation_key"]["max_length"],
        unique=True,
        validators=[MinLengthValidator(settings.FIELD_META["confirmation_key"]["min_length"])],
    )
    expires_at = models.DateTimeField(_("key expiry"))

    class Meta:
        verbose_name = _("confirmation key")
        verbose_name_plural = _("confirmation keys")


__all__ = ["ConfirmationKey"]
