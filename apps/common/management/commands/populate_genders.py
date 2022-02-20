from django.core.management.base import BaseCommand

from apps.common.models import Gender


def populate_genders():
    items = [
        "Male",
        "Female",
    ]
    item_instances = []

    for item in items:
        item_instances.append(Gender(name=item))

    Gender.objects.bulk_create(item_instances, ignore_conflicts=True)


class Command(BaseCommand):
    help = "Populate genders."

    def handle(self, *args, **options):
        del args, options

        populate_genders()
