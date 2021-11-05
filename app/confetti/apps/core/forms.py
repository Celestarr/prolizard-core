from django import forms
from django.conf import settings
from django.contrib.auth import authenticate, get_user_model, password_validation
from django.contrib.auth.forms import AuthenticationForm as BaseAuthenticationForm
from django.core.exceptions import ValidationError
from django.utils.text import capfirst
from django.utils.translation import gettext_lazy as _


class AuthenticationForm(BaseAuthenticationForm):
    email = forms.EmailField(
        widget=forms.EmailInput(attrs={"autofocus": True, "class": "form-control", "placeholder": "a@a.com"})
    )
    password = forms.CharField(
        label=_("Password"),
        strip=False,
        widget=forms.PasswordInput(
            attrs={
                "autocomplete": "current-password",
                "class": "form-control",
            }
        ),
    )
    remember_me = forms.BooleanField(widget=forms.CheckboxInput(), required=False)
    error_messages = {
        "invalid_login": _("Please enter a correct U and password. Note that both " "fields may be case-sensitive."),
        "inactive": _("This account is inactive."),
    }

    def __init__(self, request, *args, **kwargs):
        super().__init__(request, *args, **kwargs)

        del self.fields["username"]

        # Set the max length and label for the "email" field.
        self.fields["email"].max_length = settings.FIELD_META["email"]["max_length"]
        self.fields["email"].widget.attrs["maxlength"] = settings.FIELD_META["email"]["max_length"]
        if self.fields["email"].label is None:
            self.fields["email"].label = capfirst(_("email"))
        self.label_suffix = ""

    def clean(self):
        email = self.cleaned_data.get("email")
        password = self.cleaned_data.get("password")

        if email is not None and password:
            self.user_cache = authenticate(self.request, email=email, password=password)
            if self.user_cache is None:
                raise self.get_invalid_login_error()
            else:
                self.confirm_login_allowed(self.user_cache)

        return self.cleaned_data

    def get_invalid_login_error(self):
        return ValidationError(
            self.error_messages["invalid_login"],
            code="invalid_login",
            params={"email": "email"},
        )


class AdminAuthenticationForm(AuthenticationForm):
    """
    A custom authentication form used in the admin app.
    """

    error_messages = {
        **AuthenticationForm.error_messages,
        "invalid_login": _(
            "Please enter the correct U and password for a staff "
            "account. Note that both fields may be case-sensitive."
        ),
    }
    required_css_class = "required"

    def confirm_login_allowed(self, user):
        super().confirm_login_allowed(user)
        if not user.is_staff:
            raise ValidationError(
                self.error_messages["invalid_login"], code="invalid_login", params={"email": "email"}
            )
