import json

from django.conf import settings
from django.core.management.base import BaseCommand

from app.apps.core.models import SupportedLocale


def populate_locales():
    src_file = settings.DATA_DIR / "json" / "locales.json"
    supported_locales = json.loads(src_file.read_text())
    new_items = []

    for item in supported_locales:
        queryset = SupportedLocale.objects.filter(locale_tag=item["locale_tag"])
        payload = {
            "locale_tag": item["locale_tag"],
            "iso_639_1_code": item["iso_639_1_code"],
            "iso_639_2_code": item["iso_639_2_code"],
            "name": item["name"],
            "native_name": item["native_name"],
        }

        if queryset.exists():
            queryset.update(**payload)
        else:
            new_items.append(SupportedLocale(**payload))

    SupportedLocale.objects.bulk_create(new_items, ignore_conflicts=True)


class Command(BaseCommand):
    help = "Populate locales."

    def handle(self, *args, **options):
        del args, options

        populate_locales()
