from typing import List

from django.contrib.auth.hashers import make_password
from django.core.management.base import BaseCommand
from faker import Faker

from apps.core.models.user import User

fake = Faker(["fr_FR", "de_DE", "ja_JP", "zh_CN", "en_US", "hi_IN"])


def generate_users() -> List[User]:
    users = []
    password = make_password("123456")

    for i in range(50):
        users.append(
            User(
                first_name=fake.unique.first_name(),
                last_name=fake.unique.last_name(),
                email=fake.unique.ascii_free_email(),
                password=password,
                username="0000{}".format(i),
                user_type="Staff",
            )
        )

    for i in range(200):
        users.append(
            User(
                first_name=fake.unique.first_name(),
                last_name=fake.unique.last_name(),
                email=fake.unique.ascii_free_email(),
                password=password,
                username="1000{}".format(i),
                user_type="Member",
            )
        )

    return users


class Command(BaseCommand):
    help = "Populate database with fake data. Useful for development environment."

    # def add_arguments(self, parser):
    #     parser.add_argument('poll_ids', nargs='+', type=int)

    def handle(self, *args, **options):
        print("Creating bulk users...")
        users = generate_users()
        User.objects.bulk_create(users, ignore_conflicts=True)
