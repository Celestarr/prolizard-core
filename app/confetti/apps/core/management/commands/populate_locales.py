import json
from pathlib import Path

from django.conf import settings
from django.core.management.base import BaseCommand

from confetti.apps.core.models import Language, Locale


def populate_locales():
    src_dir = settings.DATA_DIR / "json" / "locale"
    new_items = []

    for src_file in src_dir.iterdir():
        item = json.loads(src_file.absolute().read_text().strip() or "{}")
        qs = Locale.objects.filter(locale_tag=item["locale_tag"])

        try:
            item["language"] = Language.objects.get(iso_639_2_code=item["iso_639_2_code"])
            del item["iso_639_2_code"]
        except Language.DoesNotExist:
            continue

        if qs.exists():
            qs.update(**item)
        else:
            new_items.append(Locale(**item))

    Locale.objects.bulk_create(new_items, ignore_conflicts=True)


class Command(BaseCommand):
    help = "Populate locales."

    def handle(self, *args, **options):
        del args, options

        populate_locales()
