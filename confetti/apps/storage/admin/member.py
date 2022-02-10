from django.contrib import admin
from django.urls import reverse
from django.utils.html import format_html
from django.utils.translation import gettext_lazy as _

from ..models import MemberResume


@admin.register(MemberResume)
class MemberResumeAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "link_to_edit_member",
        "pdf",
        "version",
        "updated_at",
    )
    ordering = ("-id",)

    def link_to_edit_member(self, obj):
        link = reverse("admin:core_user_change", args=[obj.member_id])
        return format_html('<a href="{}">{}</a>', link, obj.member.email)

    link_to_edit_member.short_description = _("Member")


__all__ = ["MemberResumeAdmin"]
