from django.contrib.auth import get_user_model
from django.contrib.auth.backends import ModelBackend as BaseModelBackend

UserModel = get_user_model()


class ModelBackend(BaseModelBackend):
    def authenticate(self, request, username=None, password=None, **kwargs):
        del request

        identifier = kwargs.get("email", username)

        if password is None or identifier is None:
            return

        try:
            query_kwargs = {}

            if "@" in identifier:
                query_kwargs["email"] = identifier
            else:
                query_kwargs["username"] = identifier

            user = UserModel.objects.get(**query_kwargs)
        except UserModel.DoesNotExist:
            # Run the default password hasher once to reduce the timing
            # difference between an existing and a nonexistent user (#20760).
            UserModel().set_password(password)

        else:
            if user.check_password(password) and self.user_can_authenticate(user):
                return user
