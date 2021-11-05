from django.conf import settings
from django.core.management.base import BaseCommand

from confetti.apps.member.models import ResumeTemplate
from confetti.utils import snake_case_to_title

TEMPLATE_PUPPETEER_CONFIGS = {
    "Chicago Gray": {
        "format": "a4",
        "printBackground": True,
        "margin": {
            "bottom": "0.75in",
            "left": "1in",
            "right": "1in",
            "top": "0.75in",
        },
    },
    "Engineering Ultimate": {
        "format": "a4",
        "printBackground": True,
        "margin": {
            "bottom": "0.75in",
            "left": "0.75in",
            "right": "0.75in",
            "top": "0.75in",
        },
    },
}


def populate_resume_templates():
    src_dir = settings.DATA_DIR / "pug" / "templates" / "resume"
    new_items = []
    name_transformer = lambda x: x.split(".")[0]

    for src_file in src_dir.iterdir():
        src_file_name = src_file.name

        if src_file_name == ".gitkeep":
            continue

        qs = ResumeTemplate.objects.filter(template_file_name=src_file_name)

        if not qs.exists():
            template_name = snake_case_to_title(src_file_name, transformer=name_transformer)
            new_items.append(
                ResumeTemplate(
                    name=template_name,
                    template_file_name=src_file_name,
                    puppeteer_config=TEMPLATE_PUPPETEER_CONFIGS.get(template_name, {}),
                )
            )

    ResumeTemplate.objects.bulk_create(new_items, ignore_conflicts=True)


class Command(BaseCommand):
    help = "Populate resume templates."

    def handle(self, *args, **options):
        del args, options

        populate_resume_templates()
