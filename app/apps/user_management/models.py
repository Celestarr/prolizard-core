from django.conf import settings
from django.contrib.auth.models import AbstractUser
from django.core.validators import MinLengthValidator
from django.db import models
from django.utils.translation import gettext_lazy as _

from app.utils.db.models import TimeStampedModel

from .validators import UsernameValidator


class User(AbstractUser, TimeStampedModel):
    """
    Users within the Django authentication system are represented by this
    model. This is a custom, fully featured User model with admin-compliant
    permissions.
    """

    username_validator = UsernameValidator()

    about = models.CharField(blank=True, max_length=1000, null=True)
    address = models.CharField(blank=True, max_length=250, null=True)
    country = models.ForeignKey(
        "core.Country",
        blank=True,
        null=True,
        on_delete=models.SET_NULL,
        related_name="user_set",
    )
    date_of_birth = models.DateField(blank=True, null=True)
    email = models.EmailField(
        _("email address"),
        blank=True,
        max_length=settings.FIELD_META["email"]["max_length"],
        unique=True,
        error_messages={
            "blank": _("Enter a valid email address."),
            "invalid": _("Enter a valid email address."),
            "unique": _("Email is invalid or already taken."),
        },
    )
    first_name = models.CharField(
        _("first name"),
        blank=True,
        max_length=settings.FIELD_META["first_name"]["max_length"],
        validators=[MinLengthValidator(settings.FIELD_META["first_name"]["min_length"])],
    )

    GENDER_CHOICES = [
        ("MALE", "Male"),
        ("FEMALE", "Female"),
        ("OTHER", "Other"),
    ]
    gender = models.CharField(
        blank=True,
        choices=GENDER_CHOICES,
        max_length=20,
        null=True,
    )

    headline = models.CharField(blank=True, max_length=250, null=True)
    is_active = models.BooleanField(
        _("active"),
        blank=True,
        default=False,
        help_text=_(
            "Designates whether this user should be treated as active. Unselect this instead of deleting accounts."
        ),
    )
    last_name = models.CharField(
        _("last name"),
        blank=True,
        max_length=settings.FIELD_META["last_name"]["max_length"],
        validators=[MinLengthValidator(settings.FIELD_META["last_name"]["min_length"])],
    )
    password = models.CharField(_("password"), blank=True, max_length=128)
    username = models.CharField(
        _("username"),
        blank=True,
        max_length=settings.FIELD_META["username"]["max_length"],
        unique=True,
        help_text=_("Required. 3 to 30 characters. Letters (a-z), digits (0-9) and underscore (_) only."),
        validators=[MinLengthValidator(1), username_validator],
        error_messages={
            "unique": _("A user with that username already exists."),
        },
    )

    user_editable_fields = [
        "about",
        "address",
        "country",
        "date_of_birth",
        "first_name",
        "gender",
        "headline",
        "last_name",
    ]

    # Invalidate unused fields
    # date_joined = None
    # last_login = None  # used by django-oauth-toolkit

    class Meta(AbstractUser.Meta):
        swappable = "AUTH_USER_MODEL"

    def get_form_layout_config(self):
        return [
            {"row": 1, "fields": ["first_name", "last_name"], "sizes": [6, 6]},
            {"row": 2, "fields": ["gender", "date_of_birth"], "sizes": [6, 6]},
            {"row": 3, "fields": ["address", "country"], "sizes": [6, 6]},
            {"row": 4, "fields": ["headline"], "sizes": [12]},
            {"row": 5, "fields": ["about"], "sizes": [12]},
        ]

    @property
    def location(self):
        if self.address and self.country:
            return f"{self.address}, {self.country}"

        return self.address or self.country or None

    def save(self, *args, **kwargs):
        self.email = self.email.lower()

        return super().save(*args, **kwargs)
