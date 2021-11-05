from django.db import models
from django.utils.translation import gettext_lazy as _

from confetti.apps.core import models
from confetti.apps.core.models import TimeStampedModel


class MemberResume(TimeStampedModel):
    member = models.OneToOneField("core.User", on_delete=models.CASCADE, related_name="member_resume")
    download_url = models.CharField(max_length=250, blank=True, null=True)
    version = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        verbose_name = _("member résumé")
        verbose_name_plural = _("member résumés")


__all__ = ["MemberResume"]
