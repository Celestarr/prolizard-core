from django.conf import settings
from django.contrib.auth.views import LoginView as BaseLoginView
from django.contrib.auth.views import LogoutView as BaseLogoutView
from django.db import transaction
from django.forms import ModelForm
from django.http import HttpRequest, HttpResponseRedirect
from django.urls import reverse
from django.views.generic import CreateView

from app.apps.profile.models import UserPreference
from app.apps.user_management.models import User

from .forms import AuthenticationForm, UserRegistrationForm


class RegistrationView(CreateView):
    template_name = "apps/user_management/registration.html"
    success_template_name = "apps/user_management/registration_success.html"
    model = User
    form_class = UserRegistrationForm

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.object = None

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        return {
            **ctx,
            "APP_LOGIN_URL": settings.APP_LOGIN_URL,
        }

    @transaction.atomic
    def form_valid(self, form: ModelForm):
        self.object = form.save()
        UserPreference.objects.create(user=form.save())

    def post(self, request, *args, **kwargs):
        """
        Handle POST requests: instantiate a form instance with the passed
        POST variables and then check if it's valid.
        """
        form = self.get_form()

        if form.is_valid():
            self.form_valid(form)

            # replace primary template with success template
            self.template_name = self.success_template_name

            return self.render_to_response(self.get_context_data())

        print(form.non_field_errors(), form.errors)
        print(form.data)
        return self.render_to_response(self.get_context_data())


class LoginView(BaseLoginView):
    form_class = AuthenticationForm
    template_name = "apps/user_management/login.html"
    redirect_authenticated_user = True

    def form_valid(self, form):
        remember_me = form.cleaned_data["remember_me"]  # get remember me data from cleaned_data of form

        if not remember_me:
            self.request.session.set_expiry(0)  # if remember me is
            self.request.session.modified = True

        return super().form_valid(form)


class LogoutView(BaseLogoutView):
    pass


def auth0_token_redirect_view(request: HttpRequest) -> HttpResponseRedirect:
    del request
    return HttpResponseRedirect(reverse("oauth2_provider:token"))
