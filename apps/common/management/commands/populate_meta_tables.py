from django.core.management import call_command
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    help = "Populate database meta tables that hold pre-defined data."

    def handle(self, *args, **options):
        del args, options

        call_command("populate_currencies")
        call_command("populate_locales")
        call_command("populate_time_zones")
        call_command("populate_countries")
        call_command("populate_genders")
        call_command("populate_employment_types")
        call_command("populate_proficiency_levels")
        call_command("populate_resume_templates")
