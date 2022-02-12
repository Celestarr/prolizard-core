from django.contrib import admin

from ..models import MemberPreference


@admin.register(MemberPreference)
class MemberPreferenceAdmin(admin.ModelAdmin):
    pass
