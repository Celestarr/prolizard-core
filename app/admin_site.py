from django.contrib.admin import AdminSite as BaseAdminSite
from django.utils.translation import gettext_lazy as _

from app.apps.identity.forms import AdminAuthenticationForm


class AdminSite(BaseAdminSite):
    site_title = _("ProLizard Admin Panel")
    site_header = _("ProLizard Administration")
    index_title = _("ProLizard Administration")
    empty_value_display = "N/A"

    login_form = AdminAuthenticationForm
    login_template = "core/admin/login.html"
