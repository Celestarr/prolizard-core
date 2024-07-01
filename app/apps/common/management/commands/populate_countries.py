# pylint: disable=duplicate-code
import pycountry
from django.core.management.base import BaseCommand

from app.apps.common.models import Country


def populate_countries():
    new_items = []

    for item in pycountry.countries:
        queryset = Country.objects.filter(iso_3166_1_alpha_3_code=item.alpha_3)

        payload = {
            "iso_3166_1_alpha_2_code": item.alpha_2,
            "iso_3166_1_alpha_3_code": item.alpha_3,
            "iso_3166_1_numeric_code": item.numeric,
            "name": item.name,
            # Fallback to short/display name if official name is
            # not provided.
            "formal_name": getattr(item, "official_name", item.name),
        }

        if queryset.exists():
            queryset.update(**payload)
        else:
            new_items.append(Country(**payload))

    Country.objects.bulk_create(new_items, ignore_conflicts=True)


class Command(BaseCommand):
    help = "Populate countries."

    def handle(self, *args, **options):
        del args, options

        populate_countries()
