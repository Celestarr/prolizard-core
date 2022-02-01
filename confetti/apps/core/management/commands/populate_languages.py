import json
from pathlib import Path

from django.conf import settings
from django.core.management.base import BaseCommand

from confetti.apps.core.models import Language


def populate_languages():
    src_dir = settings.DATA_DIR / "json" / "language"
    new_items = []

    for src_file in src_dir.iterdir():
        item = json.loads(src_file.absolute().read_text().strip() or "{}")
        qs = Language.objects.filter(iso_639_2_code=item["iso_639_2_code"])

        if qs.exists():
            qs.update(**item)
        else:
            new_items.append(Language(**item))

    Language.objects.bulk_create(new_items, ignore_conflicts=True)


class Command(BaseCommand):
    help = "Populate languages."

    def handle(self, *args, **options):
        del args, options

        populate_languages()
