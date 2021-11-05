from django.contrib import admin
from django.utils.translation import gettext
from django.utils.translation import gettext_lazy as _

from ..models import UserEmail


@admin.register(UserEmail)
class UserEmailAdmin(admin.ModelAdmin):
    pass
