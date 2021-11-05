from django.core import validators
from django.utils.deconstruct import deconstructible
from django.utils.translation import gettext_lazy as _


@deconstructible
class UsernameValidator(validators.RegexValidator):
    # regex = r"^[A-Za-z][-09A-Za-z_]+[A-Za-z]$"
    regex = r"^[0-9A-Za-z_]+$"
    message = _(
        "Enter a valid username. This value may contain only letters (a-z), " "numbers (0-9), and underscore (_)."
    )
    flags = 0
