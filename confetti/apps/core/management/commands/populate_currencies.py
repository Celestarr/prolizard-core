import json
from pathlib import Path

from django.conf import settings
from django.core.management.base import BaseCommand

from confetti.apps.core.models import Currency


def populate_currencies():
    src_file = settings.DATA_DIR / "json" / "currencies.json"
    currencies = json.loads(src_file.read_text())
    new_items = []

    for item in currencies:
        qs = Currency.objects.filter(iso_4217_code=item["iso_4217_code"])
        payload = {
            "iso_4217_code": item["iso_4217_code"],
            "iso_4217_numeric_code": item["iso_4217_numeric_code"],
            "name": item["name"],
            "symbol": item["symbol"],
        }

        if qs.exists():
            qs.update(**payload)
        else:
            new_items.append(Currency(**payload))

    Currency.objects.bulk_create(new_items, ignore_conflicts=True)


class Command(BaseCommand):
    help = "Populate currencies."

    def handle(self, *args, **options):
        del args, options

        populate_currencies()
