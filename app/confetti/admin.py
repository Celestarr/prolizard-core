from django.contrib.admin import AdminSite as BaseAdminSite
from django.utils.translation import gettext
from django.utils.translation import gettext_lazy as _

from confetti.apps.core.forms import AdminAuthenticationForm


class AdminSite(BaseAdminSite):
    site_title = _("Confetti Admin Panel")
    site_header = _("Confetti Administration")
    index_title = _("Confetti Administration")
    empty_value_display = "N/A"

    login_form = AdminAuthenticationForm
    login_template = "core/admin/login.html"


__all__ = ["AdminSite"]
