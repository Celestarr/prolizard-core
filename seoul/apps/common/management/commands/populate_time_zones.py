import json

from django.conf import settings
from django.core.management.base import BaseCommand

from seoul.apps.common.models import TimeZone


def populate_time_zones():
    src_file = settings.DATA_DIR / "json" / "time_zones.json"
    time_zones = json.loads(src_file.read_text())
    new_items = []

    for item in time_zones:
        queryset = TimeZone.objects.filter(name=item["name"])
        payload = {
            "abbreviation": item["abbreviation"],
            "name": item["name"],
            "offset_display_text": item["offset_display_text"],
            "offset_text": item["offset_text"],
            "offset_text_clean": item["offset_text_clean"],
            "offset_minutes": item["offset_minutes"],
        }

        if queryset.exists():
            queryset.update(**payload)
        else:
            new_items.append(TimeZone(**payload))

    TimeZone.objects.bulk_create(new_items, ignore_conflicts=True)


class Command(BaseCommand):
    help = "Populate time zones."

    def handle(self, *args, **options):
        del args, options

        populate_time_zones()
