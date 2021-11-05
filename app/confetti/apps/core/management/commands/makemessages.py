from django.core.management.commands.makemessages import Command as BaseCommand


class Command(BaseCommand):
    """Custom makemessages command that disables fuzzy translation."""

    msgmerge_options = ["-q", "--previous", "--no-fuzzy-matching"]
