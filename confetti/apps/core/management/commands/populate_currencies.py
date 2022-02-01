import json
from pathlib import Path

from django.conf import settings
from django.core.management.base import BaseCommand

from confetti.apps.core.models import Currency


def populate_currencies():
    src_dir = settings.DATA_DIR / "json" / "currency"
    new_items = []

    for src_file in src_dir.iterdir():
        item = json.loads(src_file.absolute().read_text().strip() or "{}")
        qs = Currency.objects.filter(iso_4217_code=item["iso_4217_code"])

        if qs.exists():
            qs.update(**item)
        else:
            new_items.append(Currency(**item))

    Currency.objects.bulk_create(new_items, ignore_conflicts=True)


class Command(BaseCommand):
    help = "Populate currencies."

    def handle(self, *args, **options):
        del args, options

        populate_currencies()
