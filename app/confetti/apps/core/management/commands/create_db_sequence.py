from django.core.management.base import BaseCommand
from django.db import connection
from django.db.utils import ProgrammingError


class Command(BaseCommand):
    help = "Create a database sequence."

    def add_arguments(self, parser):
        parser.add_argument("--name", nargs=None, type=str)
        parser.add_argument("--increment", nargs="?", const=1, type=int)
        parser.add_argument("--start", nargs="?", const=1, type=int)

    def handle(self, *args, **options):
        del args

        name = options.get("name")
        increment = options.get("increment")
        start = options.get("start")

        if not name and not increment or not start:
            print("ERROR: name, increment or start is missing")
            return

        try:
            with connection.cursor() as cursor:
                cursor.execute("CREATE SEQUENCE {} INCREMENT {} START {};".format(name, increment, start))
                print("SUCCESS: sequence created")
        except ProgrammingError as e:
            print("ERROR: {}".format(str(e)))
