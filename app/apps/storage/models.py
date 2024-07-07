from django.db import models
from django.utils.translation import gettext_lazy as _

from app.utils.db.models import TimeStampedModel


def generate_resume_upload_path(instance, filename):
    del instance
    return f"resume/{filename}"


class Resume(TimeStampedModel):
    user = models.OneToOneField("identity.User", on_delete=models.CASCADE, related_name="resume")
    pdf = models.FileField(max_length=300, blank=True, null=True, upload_to=generate_resume_upload_path)
    version = models.CharField(max_length=300, blank=True, null=True)

    class Meta:
        verbose_name = _("résumé")
        verbose_name_plural = _("résumés")
