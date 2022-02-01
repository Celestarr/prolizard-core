from django.contrib.auth.views import LoginView as BaseLoginView
from django.db import transaction
from django.forms import ModelForm
from django.views.generic import CreateView

from confetti.apps.core.models import User
from confetti.apps.core.models.utils import get_username_sequence_value
from confetti.apps.member.models.preference import MemberPreference
from confetti.utils.ds import update_immutable_querydict

from .forms import AuthenticationForm


class RegistrationView(CreateView):
    template_name = "identity/registration.html"
    success_template_name = "identity/registration_success.html"
    model = User
    fields = ("first_name", "last_name", "email", "is_active", "password", "username")

    @transaction.atomic
    def form_valid(self, form: ModelForm):
        self.object = form.save()
        MemberPreference.objects.create(user=self.object)

    def get(self, request, *args, **kwargs):
        self.object = None
        return super().get(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        """
        Handle POST requests: instantiate a form instance with the passed
        POST variables and then check if it's valid.
        """
        self.object = None

        form = self.get_form()

        update_immutable_querydict(form.data, "is_active", True)  # TODO: decide later
        update_immutable_querydict(form.data, "username", get_username_sequence_value())

        if form.is_valid():
            self.form_valid(form)

            # replace primary template with success template
            self.template_name = self.success_template_name

            return self.render_to_response(self.get_context_data())
        else:
            print(form.non_field_errors(), form.errors)
            print(form.data)
            return self.render_to_response(self.get_context_data())


class LoginView(BaseLoginView):
    form_class = AuthenticationForm
    template_name = "identity/login.html"
    redirect_authenticated_user = True

    def form_valid(self, form):
        remember_me = form.cleaned_data["remember_me"]  # get remember me data from cleaned_data of form

        if not remember_me:
            self.request.session.set_expiry(0)  # if remember me is
            self.request.session.modified = True

        return super().form_valid(form)
