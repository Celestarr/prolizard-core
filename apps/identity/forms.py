from django import forms
from django.conf import settings
from django.contrib.auth import authenticate, password_validation
from django.contrib.auth.forms import AuthenticationForm as BaseAuthenticationForm
from django.core.exceptions import ValidationError
from django.utils.text import capfirst
from django.utils.translation import gettext_lazy as _

from apps.core.models import User
from apps.core.models.utils import get_username_sequence_value


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
                self.error_messages["invalid_login"],
                code="invalid_login",
                params={"email": "email"},
            )


class UserRegistrationForm(forms.ModelForm):
    """
    A form that creates a user, with no privileges, from the given username and
    password.
    """

    error_messages = {
        "password_mismatch": _("The two password fields didn’t match."),
    }
    password = forms.CharField(
        label=_("Password"),
        strip=False,
        widget=forms.PasswordInput(attrs={"autocomplete": "new-password"}),
        help_text=password_validation.password_validators_help_text_html(),
    )

    class Meta:
        model = User
        fields = ("first_name", "last_name", "email", "password")

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if self._meta.model.USERNAME_FIELD in self.fields:
            self.fields[self._meta.model.USERNAME_FIELD].widget.attrs["autofocus"] = True

    def _post_clean(self):
        super()._post_clean()
        # Validate the password after self.instance is updated with form data
        # by super().
        password = self.cleaned_data.get("password")
        if password:
            try:
                password_validation.validate_password(password, self.instance)
            except ValidationError as error:
                self.add_error("password", error)

    def save(self, commit=True):
        self.instance.is_active = True
        self.instance.username = get_username_sequence_value()
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password"])
        if commit:
            user.save()
        return user
