import json
from pathlib import Path

from django.conf import settings
from django.core.management.base import BaseCommand
from django.db.utils import IntegrityError

from confetti.apps.core.models import Country


def populate_countries():
    src_dir = settings.DATA_DIR / "json" / "territory"
    new_items = []

    for src_file in src_dir.iterdir():
        item = json.loads(src_file.absolute().read_text().strip() or "{}")
        qs = Country.objects.filter(iso_3166_1_alpha_3_code=item["iso_3166_1_alpha_3_code"])

        if qs.exists():
            qs.update(**item)
        else:
            new_items.append(Country(**item))

    Country.objects.bulk_create(new_items, ignore_conflicts=True)


class Command(BaseCommand):
    help = "Populate countries."

    def handle(self, *args, **options):
        del args, options

        populate_countries()
