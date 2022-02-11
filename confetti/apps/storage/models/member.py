from django.db import models
from django.utils.translation import gettext_lazy as _

from confetti.apps.core.models import TimeStampedModel


def generate_cv_upload_path(instance, filename):
    return f"cv/{filename}"


class MemberResume(TimeStampedModel):
    member = models.OneToOneField("core.User", on_delete=models.CASCADE, related_name="member_resume")
    pdf = models.FileField(max_length=300, blank=True, null=True, upload_to=generate_cv_upload_path)
    version = models.CharField(max_length=300, blank=True, null=True)

    class Meta:
        verbose_name = _("member résumé")
        verbose_name_plural = _("member résumés")


__all__ = ["MemberResume"]
