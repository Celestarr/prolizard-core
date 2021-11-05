from django.contrib.auth.views import LoginView
from django.views.generic.edit import FormView

from confetti.apps.core.forms import AuthenticationForm


class SignInView(LoginView):
    form_class = AuthenticationForm
    template_name = "core/auth/sign-in.html"
    redirect_authenticated_user = True

    def form_valid(self, form):
        remember_me = form.cleaned_data["remember_me"]  # get remember me data from cleaned_data of form

        if not remember_me:
            self.request.session.set_expiry(0)  # if remember me is
            self.request.session.modified = True

        return super().form_valid(form)


class SignUpView(FormView):
    template_name = "core/auth/sign-up.html"


__all__ = ["SignInView", "SignUpView"]
