from django.db import models
from django.utils.translation import gettext_lazy as _


class TimeStampedModel(models.Model):
    created_at = models.DateTimeField(_("creation time"), auto_now_add=True)
    updated_at = models.DateTimeField(_("last update time"), auto_now=True)

    objects = models.Manager()

    class Meta:
        abstract = True


class SmallTimeStampedModel(TimeStampedModel):
    id = models.SmallAutoField(primary_key=True)

    class Meta:
        abstract = True


__all__ = ["TimeStampedModel", "SmallTimeStampedModel"]
