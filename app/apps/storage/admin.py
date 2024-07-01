from django.contrib import admin
from django.urls import reverse
from django.utils.html import format_html
from django.utils.translation import gettext_lazy as _

from app.apps.common.admin import ReadOnlyModelAdmin

from .models import Resume


@admin.register(Resume)
class ResumeAdmin(ReadOnlyModelAdmin):
    list_display = (
        "id",
        "link_to_edit_user",
        "pdf",
        "version",
        "updated_at",
    )
    ordering = ("-id",)

    def link_to_edit_user(self, obj):
        link = reverse("admin:core_user_change", args=[obj.user_id])
        return format_html('<a href="{}">{}</a>', link, obj.user.email)

    link_to_edit_user.short_description = _("User")
