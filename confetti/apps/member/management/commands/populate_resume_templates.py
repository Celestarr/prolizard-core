from django.conf import settings
import json
from django.core.management.base import BaseCommand

from confetti.apps.member.models import ResumeTemplate


def populate_resume_templates():
    src_dir = settings.BASE_DIR / "templates" / "latex"
    new_items = []

    for item in src_dir.iterdir():
        if item.is_file():
            continue

        dir_name = item.name
        definition = None
        entrypoint = None

        for dir_file in item.iterdir():
            if not dir_file.is_file():
                continue

            file_name = dir_file.name

            if file_name != 'definition.json':
                continue

            definition = json.loads(dir_file.read_text())

            if definition['type'] != 'cv':
                break

            entrypoint = definition['entrypoint']
            break

        if not definition or not entrypoint:
            continue

        qs = ResumeTemplate.objects.filter(slug=dir_name)

        if not qs.exists():
            new_items.append(
                ResumeTemplate(
                    slug=dir_name,
                    name=definition['name'],
                    template_entrypoint=entrypoint,
                )
            )

    ResumeTemplate.objects.bulk_create(new_items, ignore_conflicts=True)


class Command(BaseCommand):
    help = "Populate resume templates."

    def handle(self, *args, **options):
        del args, options

        populate_resume_templates()
