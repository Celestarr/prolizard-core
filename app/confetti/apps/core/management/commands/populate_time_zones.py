import json
from pathlib import Path

from django.conf import settings
from django.core.management.base import BaseCommand

from confetti.apps.core.models import TimeZone


def populate_time_zones():
    src_dir = settings.DATA_DIR / "json" / "time_zone"
    new_items = []

    for src_file in src_dir.iterdir():
        items = json.loads(src_file.absolute().read_text().strip() or "[]")

        for item in items:
            qs = TimeZone.objects.filter(name=item["name"])

            if qs.exists():
                qs.update(**item)
            else:
                new_items.append(TimeZone(**item))

    TimeZone.objects.bulk_create(new_items, ignore_conflicts=True)


class Command(BaseCommand):
    help = "Populate time zones."

    def handle(self, *args, **options):
        del args, options

        populate_time_zones()
