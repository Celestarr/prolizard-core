from django.core.management.base import BaseCommand
from django.db import IntegrityError

from apps.identity.models import User
from utils.db import get_username_sequence_value


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
            print("Email or password missing.")
            return

        username = str(get_username_sequence_value())

        try:
            User.objects.create_superuser(username, email, password, is_active=True)
            print(f"Superuser has been created successfully (username: {username}).")
        except IntegrityError as exception:
            print(f"Superuser could not be created (reason: {str(exception)}).")
