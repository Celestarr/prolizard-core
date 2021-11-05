from django.conf import settings
from django.core.validators import MinLengthValidator
from django.db import models
from django.utils.translation import gettext_lazy as _

from .common import TimeStampedModel


class UserEmail(TimeStampedModel):
    confirmation_key = models.OneToOneField(
        "ConfirmationKey", on_delete=models.SET_NULL, null=True, related_name="user_email"
    )
    email = models.EmailField(
        _("email address"),
        blank=True,
        max_length=settings.FIELD_META["email"]["max_length"],
        unique=True,
    )
    is_verified = models.BooleanField(_("verified or not"), blank=True, default=False)
    user = models.ForeignKey("User", on_delete=models.CASCADE, related_name="email_set")

    class Meta:
        verbose_name = _("user email")
        verbose_name_plural = _("user emails")


__all__ = ["UserEmail"]
