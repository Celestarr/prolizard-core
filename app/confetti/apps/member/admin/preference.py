from django.contrib import admin
from django.utils.translation import gettext_lazy as _

from ..models import MemberPreference


@admin.register(MemberPreference)
class MemberPreferenceAdmin(admin.ModelAdmin):
    pass
