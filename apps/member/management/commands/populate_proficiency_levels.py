from django.core.management.base import BaseCommand

from apps.member.models import LanguageProficiencyLevel, SkillProficiencyLevel


def populate_language_proficiency_levels():
    items = [
        {"label": "Elementary Proficiency", "value": 1},
        {"label": "Limited Working Proficiency", "value": 2},
        {"label": "Professional Working Proficiency", "value": 3},
        {"label": "Full Professional Proficiency", "value": 4},
        {"label": "Native/Bilingual Proficiency", "value": 5},
    ]
    item_instances = []

    for item in items:
        item_instances.append(LanguageProficiencyLevel(name=item["label"], value=item["value"]))

    LanguageProficiencyLevel.objects.bulk_create(item_instances, ignore_conflicts=True)


def populate_skill_proficiency_levels():
    items = [
        {"label": "Novice", "value": 1},
        {"label": "Advanced Beginner", "value": 2},
        {"label": "Competent", "value": 3},
        {"label": "Proficient", "value": 4},
        {"label": "Expert", "value": 5},
    ]
    item_instances = []

    for item in items:
        item_instances.append(SkillProficiencyLevel(name=item["label"], value=item["value"]))

    SkillProficiencyLevel.objects.bulk_create(item_instances, ignore_conflicts=True)


class Command(BaseCommand):
    help = "Populate skill and language proficiency levels."

    def handle(self, *args, **options):
        del args, options

        populate_language_proficiency_levels()
        populate_skill_proficiency_levels()
