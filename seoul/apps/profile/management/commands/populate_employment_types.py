from django.core.management.base import BaseCommand

from seoul.apps.profile.models import EmploymentType


def populate_employment_types():
    items = [
        "Casual",
        "Full-time",
        "Contract/Fixed term",
        "Part-time",
        "Trainee/Apprentice",
    ]
    item_instances = []

    for item in items:
        item_instances.append(EmploymentType(name=item))

    EmploymentType.objects.bulk_create(item_instances, ignore_conflicts=True)


class Command(BaseCommand):
    help = "Populate employment types."

    def handle(self, *args, **options):
        del args, options

        populate_employment_types()
