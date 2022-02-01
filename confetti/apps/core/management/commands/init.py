from django.core.management import call_command
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    help = "Init."

    def handle(self, *args, **options):
        del args, options

        call_command("create_db_sequence", name="core_users_username_seq", start=100, increment=3)
        call_command("populate_meta_tables")
