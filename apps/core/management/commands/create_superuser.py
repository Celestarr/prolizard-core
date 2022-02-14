from django.core.management.base import BaseCommand
from django.db import IntegrityError

from apps.core.models.user import User
from apps.core.models.utils import get_username_sequence_value


class Command(BaseCommand):
    help = "Create a superuser."

    def add_arguments(self, parser):
        parser.add_argument("--email", nargs=None, type=str)
        parser.add_argument("--password", nargs=None, type=str)

    def handle(self, *args, **options):
        del args

        email = options.get("email")
        password = options.get("password")

        if not email or not password:
            print("ERROR: email or password missing")
            return

        username = str(get_username_sequence_value())

        try:
            User.objects.create_superuser(username, email, password, is_active=True)
            print("SUCCESS: username={}".format(username))
        except IntegrityError as exception:
            print("ERROR: {}".format(str(exception)))
